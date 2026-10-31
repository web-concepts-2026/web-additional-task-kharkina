import socket
import json


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
    head, empty_line, body_text = text.partition("\r\n\r\n")
    lines = head.split("\r\n")
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

    status = "200 OK"
    content_type = "text/html"

    if method == "GET":
        if path == "/":
            file = open("index.html")
            html = file.read()
            file.close()
        elif path == "/page":
            page_id = "unknown"
            if "id" in query:
                page_id = query["id"]
            html = "<h1>Page" + page_id +"</h1>"
        else:
            status = "404 Not Found"
            html = "<h1>404 Not Found</h1>"
    elif method == "POST":
        content_type = "application/json"
        try:
            data = json.loads(body_text)
            answer = {"message": "got it", "you sent": data}
            html = json.dumps(answer)

        except ValueError:
            status = "400 Bad Request"
            html = json.dumps({"error": "invalid json"})
    else:
        status = "405 Method Not Allowed"
        html = "<h1>405 Method Not Allowed</h1>"

    body = html.encode()

    response = "HTTP/1.1 " + status +"\r\n"
    response += "Content-type:" + content_type +"\r\n"
    response += "Content-length: " +str(len(body)) + "\r\n"
    response += "\r\n"

    connection.sendall(response.encode() + body)
    connection.close()


