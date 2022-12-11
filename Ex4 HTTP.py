#step 1 -
const http = require('http');
const random = require('random');

const server = http.createServer((req, res) => {
  if (req.method === 'GET' && req.url === '/port') {
    // Generate a random number between 1 and 65535
    const portNumber = random.int(1, 65535);

    // Set the "Port Number" HTTP header in the response
    res.setHeader('Port Number', portNumber);

    // Send the response
    res.end(`Your port number is: ${portNumber}`);
  } else {
    // Return a 404 error if the request is not to the /port endpoint
    res.statusCode = 404;
    res.end('Not Found');
  }
});

server.listen(8080);

#challenge -
from flask import Flask
from random import randint

app = Flask(__name__)

@app.route('/port', methods=['GET'])
def get_port_number():
  # Generate a random number between 1 and 65535
  port_number = randint(1, 65535)

  # Set the "Port Number" HTTP header in the response
  response.headers['Port Number'] = port_number

  return f'Your port number is: {port_number}'

if __name__ == '__main__':
  app.run(port=8080)

#step 2 -
import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the specified port number
port = <random number>
sock.bind(('', port))

# Receive incoming data from the caller
data, addr = sock.recvfrom(1024)

# Compare the received code to the expected code
if data.decode() == "Cyber Himmelfarb":
  # Return the "Victory!" response if the code matches
  sock.sendto("Victory!".encode(), addr)
else:
  # Return the "No Entry" response if the code does not match
  sock.sendto("No Entry".encode(), addr)

# challenge -
import socket
from threading import Thread

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the specified port number
port = <random number>
sock.bind(('', port))

# Define a function to handle incoming requests
def handle_request():
  # Receive incoming data from the caller
  data, addr = sock.recvfrom(1024)

  # Compare the received code to the expected code
  if data.decode() == "Cyber Himmelfarb":
    # Return the "Victory!" response if the code matches
    sock.sendto("Victory!".encode(), addr)
  else:
    # Return the "No Entry" response if the code does not match
    sock.sendto("No Entry".encode(), addr)

# Start a new thread to run the server
server_thread = Thread(target=handle_request)
server_thread.start()


#step3 -
import socket
import json

# HTTP server address
http_server_address = ('localhost', 8080)

# Create a UDP socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send a request to the HTTP server to get the code execution port
http_request = b'GET /execution_port HTTP/1.1\r\nHost: localhost\r\n\r\n'
udp_socket.sendto(http_request, http_server_address)

# Receive the response from the HTTP server
http_response, _ = udp_socket.recvfrom(1024)

# Extract the port number from the response
response_data = json.loads(http_response.decode('utf-8'))
execution_port = response_data['execution_port']

# Send the code to the execution server
code = 'print("Hello, World!")'
udp_socket.sendto(code.encode('utf-8'), ('localhost', execution_port))

# Receive the response from the execution server
response, _ = udp_socket.recvfrom(1024)

# Print the response
print(response.decode('utf-8'))

try:
    # Send the code to the execution server
    code = 'print("Hello, World!")'
    udp_socket.sendto(code.encode('utf-8'), ('localhost', execution_port))

except Exception as e:
    # Handle the error
    print('An error occurred:', e)

