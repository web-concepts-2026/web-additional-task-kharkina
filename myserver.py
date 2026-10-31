import socket

server = socket.socket()
server.bind(("localhost", 8000))
server.listen()
print("Server is running on http://localhost:8000")

while True:
    connection, addr = server.accept()
    request = connection.recv(1024)
    if not request:
        connection.close()
        continue

    text = request.decode()
    lines = text.split("\r\n")
    method, path, version = lines[0].split(" ")

    print("Method:", method)
    print("Path:", path)
    connection.close()