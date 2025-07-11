import socket

TARGET_HOST = '192.168.0.10'
TARGET_PORT = 9999
SERVER_ADDRESS = (TARGET_HOST, TARGET_PORT)
FORMAT = 'utf-8'

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(SERVER_ADDRESS)
    payload = bytes("Hello tcp threaded server", FORMAT)
    client_socket.sendall(payload)

    server_data = client_socket.recv(1024)
    print(f'Received server data: {server_data.decode(FORMAT)}')

except Exception as err:
    print(f"Error occured, reason: {err}")

finally:
    client_socket.close()