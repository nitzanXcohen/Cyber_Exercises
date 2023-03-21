import socket

IP = '127.0.0.1'
PORT = 12345

MOVE_OPTIONS = {'up': 'UP', 'down': 'DOWN', 'right': 'RIGHT', 'left': 'LEFT'}


def move(side: str, s: socket.socket):
    if side not in MOVE_OPTIONS:
        return
    s.send(('MOVE ' + MOVE_OPTIONS[side]).encode())
    print(s.recv(128).decode())


def status(s: socket.socket):
    s.send('STATUS'.encode())
    response = s.recv(128).decode()
    print(response)
    if response.startswith('Thief is one step away from the cop'):
        move('up', s)
    elif response.startswith('Thief is one step away from the treasure'):
        move('down', s)


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    while True:
        try:
            input_str = input()
            if input_str in MOVE_OPTIONS:
                move(input_str, s)
            elif input_str == 's':
                status(s)
            elif input_str == 'esc':
                break
        except KeyboardInterrupt:
            break


if __name__ == '__main__':
    main()
