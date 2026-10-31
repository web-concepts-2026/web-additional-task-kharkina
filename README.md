# My HTTP Server

It is a basic server written in Python using socket library that reads each raw request to extract method, path query parameters, headers and body, then answers GET requests with page and POST request with JSON.

## Run it:

python3 myserver.py

Then open http://localhost:8000/

## Test POST:

curl -X POST http://localhost:8000/ -H "Content-Type: application/json" -d '{"name":"Anastasiia"}'
