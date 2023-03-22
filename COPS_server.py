import socket
import random


class GameMap:
    def __init__(self, file_path):
        self.map_table = self.load_map(file_path)
        self.thief_loc, self.cop_loc, self.treasure_loc = self.get_random_free_location(), self.get_random_free_location(), self.get_random_free_location()
        self.running = True

    def load_map(self, file_path):
        with open(file_path, 'rb') as f:
            map_bytes = f.read()
        map_size = int(map_bytes[0])
        map_data = [[int(c) for c in map_bytes[n:n + map_size]] for n in range(1, len(map_bytes), map_size)]
        return map_data

    def get_random_free_location(self):
        while True:
            x, y = random.randint(0, len(self.map_table) - 1), random.randint(0, len(self.map_table[0]) - 1)
            if self.is_free_location([x, y]):
                return [x, y]

    def is_free_location(self, loc):
        if loc[0] < 0 or loc[0] >= len(self.map_table) or loc[1] < 0 or loc[1] >= len(self.map_table[0]):
            return False
        if self.map_table[loc[0]][loc[1]] != 0:
            return False
        if loc == self.thief_loc or loc == self.cop_loc or loc == self.treasure_loc:
            return False
        return True

    def move_thief(self, direction):
        if not self.running:
            return None

        wall = False
        if direction == 'UP':
            new_loc = [self.thief_loc[0] - 1, self.thief_loc[1]]
        elif direction == 'DOWN':
            new_loc = [self.thief_loc[0] + 1, self.thief_loc[1]]
        elif direction == 'LEFT':
            new_loc = [self.thief_loc[0], self.thief_loc[1] - 1]
        elif direction == 'RIGHT':
            new_loc = [self.thief_loc[0], self.thief_loc[1] + 1]
        else:
            return 'INVALID'

        if not self.is_free_location(new_loc):
            wall = True
        else:
            self.thief_loc = new_loc

        if self.thief_loc == self.treasure_loc:
            self.running = False
            return 'WON'
        elif self.thief_loc == self.cop_loc:
            self.running = False
            return 'LOSE'
        else:
            self.move_cop()
            if self.thief_loc == self.cop_loc:
                self.running = False
                return 'LOSE'
            elif wall:
                return 'WALL'
            else:
                return 'OK'

    def move_cop(self):
        possible_moves = []
        for a in [-1, 0, 1]:
            for b in [-1, 0, 1]:
                if a == 0 and b == 0:
                    continue
                new_loc = [self.cop_loc[0] + a, self.cop_loc[1] + b]
                if self.is_free_location(new_loc):
                    possible_moves.append(new_loc)
        if not possible_moves:
            return
        self.cop_loc = random.choice(possible_moves)


    def __str__(self):
        str_table = [[str(a).replace('0', ' ').replace('1', '*') for a in r] for r in self.map_table]
        str_table[self.cop_loc[0]][self.cop_loc[1]] = 'C'
        str_table[self.thief_loc[0]][self.thief_loc[1]] = 'T'
        str_table[self.treasure_loc[0]][self.treasure_loc[1]] = 'X'
        txt = ''
        for r in str_table:
            for l in r:
                txt += l
            txt += '\n'
        return txt[:-1]

    def status(self):
        print(self)
        if self._near(self.thief_loc, self.cop_loc):
            return 'COP NEAR'
        if self._near(self.thief_loc, self.treasure_loc):
            return 'TREASURE NEAR'
        return 'GAME ON'

    @staticmethod
    def _near(loc1, loc2):
        if loc1[0] == loc2[0] and abs(loc1[1] - loc2[1]) == 1:
            return True
        if loc1[1] == loc2[1] and abs(loc1[0] - loc2[0]) == 1:
            return True
        return False



#Server
MAP_PATH = '"D:\הורדות\pacman.bin"'
PORT = 12345

def handle_client_connection(client_socket):
    map = GameMap(MAP_PATH)
    while True:
        command = client_socket.recv(128).decode()
        if command == 'STATUS':
            client_socket.send(map.status().encode())
        else:
            side = command[5:]
            try:
                ans = map.move_player(side)
            except Exception as e:
                print(f"Error: {e}")
                break
            else:
                client_socket.send(ans.encode())

def main():
    s = socket.socket()
    s.bind(('', PORT))
    s.listen(5)
    while True:
        client_socket, address = s.accept()
        handle_client_connection(client_socket)

if __name__ == '__main__':
    main()

