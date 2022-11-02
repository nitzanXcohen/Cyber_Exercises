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
import SocketServer

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

class MyUDPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        raw = data.split(':')
        if (raw[0] != 'GUESS'):
           socket.sendto('BAD FORMAT', self.client_address)
           return
        guess = raw[1].strip()
        if not is_valid(guess):
         socket.sendto('BAD NUMBER', self.client_address)
        if int(guess) == int(chosen):
         socket.sendto('WIN', self.client_address)
	 global won
         won = True
         return
        bulls = cows = 0
        for i in range(4):
         if guess[i] == chosen[i]:
            bulls += 1
         elif guess[i] in chosen:
            cows += 1
        socket.sendto('%iB%iC' % (bulls, cows), self.client_address)


HOST, PORT = "localhost", int(args.my_port)

def client():
 sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 sock.settimeout(1)
 for a in range(1, 10):
    for b in range(1, 10):
     for c in range(1, 10):
      for d in range(1, 10):
       if len(set([a,b,c,d])) < 4:
        continue
       myguess = ''.join(map(str, [a, b, c, d]))
       sock.sendto('GUESS:' + myguess, (HOST, PORT))
       received = sock.recv(1024)
       print ("Guessed:  " + str(myguess))
       print ("Received: {}\n".format(received))
       if "{}".format(received) == 'WIN':
        return

def server():
 if not is_valid(chosen):
  print ('SECRET IS NOT VALID')
  return
 server = SocketServer.UDPServer((HOST, PORT), MyUDPHandler)
 while not won:
  server.handle_request()

try:
 client()
except socket.timeout:
 server()