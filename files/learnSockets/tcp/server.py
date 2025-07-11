import os, socket
from utilityLogging import setupLogger

HOST=socket.gethostbyname(socket.gethostname())
PORT=12999
SERVER_ADDRESS = (HOST, PORT)
FORMAT = 'utf-8'

logger = setupLogger(log_file='talibanLogs/tcpServer.log')

def main():
    try:

        try:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.bind(SERVER_ADDRESS)
            server_socket.listen(5)
            logger.info(f"""
                Tcp server socket listening at
                    {HOST}:{PORT}
                """)
            running = True
            while running:
                client_socket, client_address = server_socket.accept()
                logger.info(f"Client connected >> [{client_address}]")
                
                client_data = True
                while client_data:
                    received_data = client_socket.recv(1024)
                    if not received_data or received_data.decode(FORMAT) == 'END':
                        break
                    logger.info(f"Client Payload: [{received_data.decode(FORMAT)}]")
                    payload = bytes("This is tcp server", FORMAT)
                    client_socket.send(payload)
                client_socket.close()

        except Exception as err:
            logger.error("Socket failed , Reason: %s"%err)

    except Exception as err:
        logger.error(f"""
            Error occured running main function !!!
                Reason: {err}
            """)
    
    

if __name__ == '__main__':
    main()