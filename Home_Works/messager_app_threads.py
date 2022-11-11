import Server_HW_comp_threads
import Client_HW
import concurrent.futures

adress = 'localhost'
comp1 = 3000
comp2 = 4000


def run_communication ():
    try:
        while True:
            msg = input('Enter message to comp2: ')
            if msg == 'stop':
                break

            Client_HW.run_client(adress, comp2, msg)

            msg = input('Enter message to comp1: ')
            if msg == 'stop':
                break

            Client_HW.run_client(adress, comp1, msg)

    except KeyboardInterrupt:
        print('Communication between comp1 and comp2 has been stopped!')

def main():

    arguments = (comp1, comp2)


    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        list(executor.map(Server_HW_comp_threads.run_server, arguments))
        run_communication ()

if __name__ == '__main__':
    main()