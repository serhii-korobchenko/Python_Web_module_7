from multiprocessing import Process
import socket
from concurrent import futures as cf
from time import sleep


def run_server(ip, port, msg_ser):  # input TCP_IP and TCP_PORT
    def handle(sock: socket.socket, address: str):  #input
        print(f'..........Connection established {address} by server.')
        while True:
            received = sock.recv(1024)
            if not received:
                break
                client_process.join()
            data = received.decode()
            print(f'>>> {data} <<< Data received from other side')
            sock.send(msg_ser.encode())
            print(f'..........Data sent by server: {msg_ser}')
        print(f'..........Socket connection closed by server {address}')
        sock.close()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # setting up socket instance
    server_socket.bind((ip, port)) # bind ip and port
    server_socket.listen(10) # set up number of listeners
    print(f'..........Start server {server_socket.getsockname()}. Start typing')
    with cf.ThreadPoolExecutor(10) as client_pool:
        try:
            while True:
                new_sock, address = server_socket.accept()

                client_pool.submit(handle, new_sock, address)  # launch def handle(sock: socket.socket, address: str)
        except KeyboardInterrupt:
            print(f'..........Destroy server')
        finally:
            server_socket.close()
            server_process.join()

def run_communication(adr, port):
    try:
        while True:
            sleep(1)
            msg = input()
            if msg == 'stop':
                server_process.terminate()
                break


            run_client(adr, port, msg)

    except KeyboardInterrupt:
        print('..........Communication between comps has been stopped!')

def run_client(ip: str, port: int, msg: str):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        server = ip, port
        sock.connect(server)
        print(f'..........Connection client established {server}')


        sock.send(msg.encode())
        sock.recv(1024)

    print(f'..........Data transfer completed by client')

if __name__ == '__main__':

    server_process = Process (target=run_server, args=('localhost', 3000, "OK")) #server initiation
    server_process.start()
    run_communication('localhost', 4000) #client initiation
