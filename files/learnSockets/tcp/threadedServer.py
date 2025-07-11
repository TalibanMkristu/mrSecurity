import socket, threading
from utilityLogging import setupLogger

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999
SERVER_ADDRESS = (HOST, PORT)
FORMAT = 'utf-8'

logger = setupLogger(log_file='talibanLogs/tcpThreadedServer.log')

def handleClients(client_socket):
    client_payload = client_socket.recv(1024)
    print(f"client payload: {client_payload.decode(FORMAT)}")
    payload = bytes("Payload received", FORMAT)
    client_socket.sendall(payload)
    client_socket.close()

def tcpServer():

    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(SERVER_ADDRESS)
        server_socket.listen(5)
        logger.info("Server socket listening on [%s:%d]", HOST, PORT)

        running =True
        while running:
            client_socket, client_address = server_socket.accept()
            print(f"Client connected: [{client_address}]")
            client_handler = threading.Thread(target=handleClients, args=(client_socket,))
            client_handler.start()

    except Exception as err:
        logger.error(str(err), exc_info=True)

def main():
    tcpServer()

if __name__ == '__main__':
    main()