import socket
HOST = '0.0.0.0'
PORT = 9999
SERVER_ADDRESS = (HOST, PORT)

def startListener():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(SERVER_ADDRESS)
    server_socket.listen(5)
    print(f"<< Listening for incoming connections [{SERVER_ADDRESS}]>>")
    while True:
        client_socket, address = server_socket.accept()
        print(f"Client connection established at {address}")
        command = input("Payload >> ")
        if command.lower() == 'exit':
            break
        client_socket.sendall(command.encode())
        client_response = client_socket.recv(4096).decode()
        print(f"Client message: {client_response}")
    client_socket.close()

def main():
    startListener()

if __name__ == '__main__':
    main()