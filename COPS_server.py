import random
import socket
import sys


class Arena:
    WALL = True
    PATH = False
    TREASURE = 'X'
    THIEF = 'T'
    COP = 'C'
    BORDER = '*'
    ARROWS = ['up', 'down', 'left', 'right']

    def __init__(self, filename):
        self.filename = filename
        self.load_arena()
        self.place_players()

    def load_arena(self):
        with open(self.filename, 'rb') as f:
            self.width = int.from_bytes(f.read(1), byteorder='little')
            self.height = int.from_bytes(f.read(1), byteorder='little')
            self.grid = [[False for j in range(self.width)] for i in range(self.height)]
            for i in range(self.height):
                for j in range(self.width):
                    self.grid[i][j] = bool(f.read(1)[0])

    def place_players(self):
        self.thief_pos = self.place_randomly()
        self.cop_pos = self.place_randomly()
        while self.cop_pos == self.thief_pos:
            self.cop_pos = self.place_randomly()
        self.treasure_pos = self.place_randomly()
        while self.treasure_pos == self.cop_pos or self.treasure_pos == self.thief_pos:
            self.treasure_pos = self.place_randomly()

    def place_randomly(self):
        i = random.randint(0, self.height - 1)
        j = random.randint(0, self.width - 1)
        while self.grid[i][j] == self.WALL:
            i = random.randint(0, self.height - 1)
            j = random.randint(0, self.width - 1)
        return (i, j)

    def move_thief(self, direction):
        new_pos = self.get_new_pos(self.thief_pos, direction)
        if self.is_valid_pos(new_pos):
            self.thief_pos = new_pos
        else:
            print('Cannot move in that direction')

    def move_cop(self):
        direction = random.choice(self.ARROWS + ['stay'])
        new_pos = self.get_new_pos(self.cop_pos, direction)
        if self.is_valid_pos(new_pos):
            self.cop_pos = new_pos

    def get_new_pos(self, pos, direction):
        i, j = pos
        if direction == 'up':
            i -= 1
        elif direction == 'down':
            i += 1
        elif direction == 'left':
            j -= 1
        elif direction == 'right':
            j += 1
        return (i, j)

    def is_valid_pos(self, pos):
        i, j = pos
        if i < 0 or j < 0 or i >= self.height or j >= self.width:
            return False
        return not self.grid[i][j]

    def is_game_over(self):
        return self.thief_pos == self.treasure_pos or self.thief_pos == self.cop_pos

    def get_status(self):
        cop_distance = self.get_distance(self.thief_pos, self.cop_pos)
        treasure_distance = self.get_distance(self.thief_pos, self.treasure_pos)
        if cop_distance == 1:
            return "You are one step away from the cop"
        elif treasure_distance == 1:
            return "You are one step away from the treasure"
        else:
            return ""

    def get_distance(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def __str__(self):
        output = ''
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j] == self.WALL:
                    output += self.BORDER
                elif (i, j) == self.thief_pos:
                    output += self.THIEF
                elif (i, j) == self.cop_pos:
                    output += self.COP
                elif (i, j) == self.treasure_pos:
                    output += self.TREASURE
                else:
                    output += self.PATH
            output += '\n'
        return output

    def handle_status_report(self):
        distance_to_cop = self.get_distance(self.thief_pos, self.cop_pos)
        distance_to_treasure = self.get_distance(self.thief_pos, self.treasure_pos)

        if distance_to_cop == 1:
            print('Thief is one step away from cop')
        elif distance_to_treasure == 0:
            print('Thief has reached the treasure!')
            return

        if distance_to_treasure == 1:
            print('Thief is one step away from the treasure')

        # Print current state of the arena
        for i in range(self.height):
            for j in range(self.width):
                if (i, j) == self.thief_pos:
                    print(self.THIEF, end='')
                elif (i, j) == self.cop_pos:
                    print(self.COP, end='')
                elif (i, j) == self.treasure_pos:
                    print(self.TREASURE, end='')
                elif self.grid[i][j] == self.WALL:
                    print(self.BORDER, end='')
                else:
                    print(self.PATH, end='')
            print()


def start_game(self):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('127.0.0.1', 12345)
    print(f'starting up on {server_address[0]} port {server_address[1]}')
    sock.bind(server_address)

    sock.listen(1)
    print('waiting for a connection...')

    while True:
        connection, client_address = sock.accept()
        print(f'connection from {client_address}')

        try:
            arena = Arena('arena.dat')
            print(arena)

            while not arena.is_game_over():
                move = connection.recv(1024).decode()
                print(f'received "{move}" from {client_address}')

                if move == 'up' or move == 'down' or move == 'left' or move == 'right':
                    arena.move_thief(move)
                elif move == 'stay':
                    pass
                else:
                    print(f'invalid move "{move}"')

                arena.move_cop()
                status = arena.get_status()
                connection.sendall(status.encode())
                arena.handle_status_report()

            if arena.thief_pos == arena.treasure_pos:
                print('You have reached the treasure!')
                connection.sendall(b'You have reached the treasure!')
            elif arena.thief_pos == arena.cop_pos:
                print('You have been caught by the cop!')
                connection.sendall(b'You have been caught by the cop!')

        finally:
            # Clean up the connection
            connection.close()

