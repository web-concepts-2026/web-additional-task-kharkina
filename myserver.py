import socket

server = socket.socket()
server.bind(("localhost", 8000))
server.listen()
print("Server is running on http://localhost:8000")

while True:
    connection, addr = server.accept()
    print("someone connected")
    connection.close()
