import socket, threading

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999
SERVER_ADDRESS = (HOST, PORT)
FORMAT = 'utf-8'

try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(SERVER_ADDRESS)

    def receiveMessages(server_socket):
        while True:
            client_message, client_address = server_socket.recvfrom(1024)
            print(f"\n [peer]: {client_message.decode(FORMAT)}")

    def sendMessage(server_socket, target_ip, target_port):
        while True:
            payload = input('Taliban >> ')
            server_socket.sendto(payload, (target_ip, target_port))
    
    target_ip = input('Enter the target ip >> ')
    target_port = int(input('Enter the target port >>'))

    threading.Thread(target=receiveMessages, args=(server_socket,)).start()
    threading.Thread(target=sendMessage, args=(server_socket,target_ip,target_port)).start()
    
except Exception as err:
    print(f"Error occured: {err}")