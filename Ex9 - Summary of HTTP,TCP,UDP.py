#step1
from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/port', methods=['GET'])
def get_port():
    port = random.randint(1024, 65535)
    return str(port), {'Port Number': str(port)}

if __name__ == '__main__':
    app.run()
    
#step2

import socket
import threading

def udp_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('', port))
    while True:
        data, address = server_socket.recvfrom(1024)
        if data.decode() == "Cyber Himmelfarb":
            server_socket.sendto(b"Victory!", address)
        else:
            server_socket.sendto(b"No Entry", address)

if __name__ == '__main__':
    port = int(input("Enter port number: "))
    t = threading.Thread(target=udp_server, args=(port,))
    t.start()


#step3

import socket
import requests

def get_port_number():
    response = requests.get('http://localhost:5000/port')
    return int(response.headers['Port Number'])

def udp_client(port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.sendto(b"Cyber Himmelfarb", ('localhost', port))
    response, address = client_socket.recvfrom(1024)
    print(response.decode())

if __name__ == '__main__':
    try:
        port = get_port_number()
        udp_client(port)
    except requests.exceptions.RequestException as e:
        print("Error connecting to the HTTP server: ", e)
    except socket.error as e:
        print("Error sending data over UDP: ", e)


