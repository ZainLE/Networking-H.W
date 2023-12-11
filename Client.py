import socket

socket_one = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 33123
server_address = '127.0.0.1'

socket_one.connect((server_address, port))

client_name=input("What is your name? ")

server_name = socket_one.recv(4096).decode()
print(f"Connected with {server_name}")


socket_one.send(client_name.encode())


while True:
    socket_one = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    port = 33123
    server_address = '127.0.0.1'

    socket_one.connect((server_address, port))
    request=input("Type your message here: ")

    socket_one.send(f"{client_name} : {request}".encode())

    buffer_size = 4096
    result = socket_one.recv(buffer_size)

    if request.lower() == "exit" or "stop":
        socket_one.send("exit".encode())
        break
    print(result.decode())