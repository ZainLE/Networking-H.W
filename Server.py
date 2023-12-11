import socket

socket_one = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 33123

socket_one.bind(("0.0.0.0", port))

socket_one.listen(10)

# name=input("What is your name? ")
print("Connect from client to continue.")

connected_socket, addr = socket_one.accept()

server_name=input("What is your name? ")

connected_socket.send(server_name.encode())

client_name = connected_socket.recv(4096).decode()

print(f"Connected with {client_name}")



while True:
    
    
    connected_socket, addr = socket_one.accept()
    
    received_data = connected_socket.recv(4096)
    print(received_data.decode())
    
    user_input=input("Type your message here: ")
    
    connected_socket.send(f"{server_name} : {user_input}".encode())
    

    if user_input.lower() == "exit" or "stop":
        connected_socket.send("exit".encode())
        break
    
socket_one.close()