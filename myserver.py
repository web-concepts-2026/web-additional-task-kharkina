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
    method, full_path, version = lines[0].split(" ")

    path, question_mark, query_string = full_path.partition("?")
    query = {}

    for x in query_string.split("&"):
        if "=" in x:
            key, value = x.split("=")
            query[key] = value

    headers = {}
    for line in lines[1:]:
        if ":" in line:
            name, value = line.split(":", 1)
            headers[name] = value.strip()


    print("Method:", method)
    print("Path:", path)
    print("Query", query)
    print("Headers", headers)
    connection.close()


