from multiprocessing import Process
import socket
from concurrent import futures as cf


def run_server(ip, port, msg):  # input TCP_IP and TCP_PORT
    def handle(sock: socket.socket, address: str):  #input
        print(f'Connection established {address}')
        while True:
            received = sock.recv(1024)
            if not received:
                break
                client_process.join()
            data = received.decode()
            print(f'Data received: {data}')
            sock.send(msg.encode())
            print(f'Data sent: {msg}')
        print(f'Socket connection closed {address}')
        sock.close()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # setting up socket instance
    server_socket.bind((ip, port)) # bind ip and port
    server_socket.listen(10) # set up number of listeners
    print(f'Start echo server {server_socket.getsockname()}')
    with cf.ThreadPoolExecutor(10) as client_pool:
        try:
            while True:
                new_sock, address = server_socket.accept()
                print (f'new_sock, address {new_sock, address}')
                client_pool.submit(handle, new_sock, address)  # launch def handle(sock: socket.socket, address: str)
        except KeyboardInterrupt:
            print(f'Destroy server')
        finally:
            server_socket.close()
            server_process.join()
            client_process.join()

def run_client(ip: str, port: int, msg: str):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        server = ip, port
        sock.connect(server)
        print(f'Connection established {server}')
        for line in msg.split(' '):
            print(f'Send data: {line}')
            sock.send(line.encode())
            response = sock.recv(1024)
            print(f'Response data: {response.decode()}')
    print(f'Data transfer completed')






if __name__ == '__main__':
    #run_server('localhost', 3000, "OK") #server initiation
    server_process = Process (target=run_server, args=('localhost', 3000, "OK")) #server initiation
    client_process = Process(target=run_client, args=('localhost', 3000, "HELLO!!!"))  #client initiation
    server_process.start()
    client_process.start()
