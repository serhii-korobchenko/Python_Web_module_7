import socket
from concurrent import futures as cf

TCP_IP = 'localhost'
TCP_PORT = 3000
MESSAGE = "OK"


def run_server(port):  # input TCP_IP and TCP_PORT
    def handle(sock: socket.socket, address: str):  #input
        print(f'Connection established {address}')
        while True:
            received = sock.recv(1024)
            if not received:
                break
            data = received.decode()
            print(f'Data received: {data}')
            sock.send(MESSAGE.encode())
            print(f'Data sent: {MESSAGE}')
        print(f'Socket connection closed {address}')
        sock.close()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # setting up socket instance
    server_socket.bind((TCP_IP, port)) # bind ip and port
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


if __name__ == '__main__':
    run_server(TCP_PORT)