#1
import random

def getDigits(num):
    return [int(i) for i in str(num)]


def noDuplicates(num):
    num_li = getDigits(num)
    if len(num_li) == len(set(num_li)):
        return True
    else:
        return False


def generateNum():
    while True:
        num = random.randint(1000, 9999)
        if noDuplicates(num):
            return num

def numOfBullsCows(num, guess):
    bull_cow = [0, 0]
    num_li = getDigits(num)
    guess_li = getDigits(guess)

    for i, j in zip(num_li, guess_li):
        if j in num_li:
            if j == i:
                bull_cow[0] += 1
            else:
                bull_cow[1] += 1
    return bull_cow

def main():
    num = generateNum()
    tries = 10
    while tries > 0:
        guess = int(input("Enter your guess: "))

        if not noDuplicates(guess):
            print("Number should not have repeated digits. Try again.")
            continue
        if guess < 1000 or guess > 9999:
            print("Enter 4 digit number only. Try again.")
            continue

        bull_cow = numOfBullsCows(num, guess)
        print(f"{bull_cow[0]} bulls, {bull_cow[1]} cows")
        tries -= 1
        if bull_cow[0] == 4:
            print("You guessed right!")
            break
    else:
        print(f"You ran out of tries. Number was {num}")
if __name__ == '__main__':
    main()







#2
import argparse
import random
import socket

parser = argparse.ArgumentParser()
parser.add_argument("number", help="the secret number")
parser.add_argument("my_port", help="the player's port")
args = parser.parse_args()
chosen = args.number

def is_valid(num):
    digits = '123456789'
    return len(num) == 4 and \
        all(char in digits for char in num) \
        and len(set(num)) == 4

won = False

def handle_guess(sock, client_address, data):
    raw = data.split(':')
    if (raw[0] != 'GUESS'):
        sock.sendto('BAD FORMAT'.encode(), client_address)
        return
    guess = raw[1].strip()
    if not is_valid(guess):
        sock.sendto('BAD NUMBER'.encode(), client_address)
        return
    if int(guess) == int(chosen):
        sock.sendto('WIN'.encode(), client_address)
        global won
        won = True
        return
    bulls = cows = 0
    for i in range(4):
        if guess[i] == chosen[i]:
            bulls += 1
        elif guess[i] in chosen:
            cows += 1
    sock.sendto('%iB%iC' % (bulls, cows), client_address)

def server():
    if not is_valid(chosen):
        print ('SECRET IS NOT VALID')
        return
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((HOST, int(args.my_port)))
    print(f"Server started on port {args.my_port}")
    while not won:
        data, client_address = sock.recvfrom(1024)
        handle_guess(sock, client_address, data)

def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(1)
    print(f"Client started on port {args.my_port}")
    for i in range(10):
        myguess = input("Enter a 4-digit number: ")
        while not is_valid(myguess):
            myguess = input("Invalid input, please enter a valid 4-digit number: ")
        sock.sendto('GUESS:' + myguess, (HOST, int(args.my_port)))
        try:
            received, server_address = sock.recvfrom(1024)
            print(f"Result: {received.decode()}")
            if "{}".format(received.decode()) == 'WIN':
                print("You won!")
                return
        except socket.timeout:
            print("No response from server.")
            return

HOST, PORT = "localhost", int(args.my_port)

if __name__ == '__main__':
    server()
    client()
