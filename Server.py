import socket

socket_one = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 33123

socket_one.bind(("0.0.0.0", port))
socket_one.listen(1)

while True:
    
    connected_socket, addr = socket_one.accept()
    print("Connection from: " + str(addr))

    received_data = connected_socket.recv(4096)
    print(received_data.decode())
    
    user_input=input("Type your message here: ")
    
    connected_socket.send(user_input.encode())
    connected_socket.close()

    if "stop" in received_data.decode():
        break

socket_one.close()

