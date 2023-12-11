import socket

while True:
    socket_one = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    port = 33123
    server_address = '127.0.0.1'

    socket_one.connect((server_address, port))
    request=input("Type your message here: ")

    socket_one.send(request.encode())

    buffer_size = 4096
    result = socket_one.recv(buffer_size)

    print(result.decode())