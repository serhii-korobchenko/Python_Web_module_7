
import Client_HW



comp1 = ('localhost', 3000)
comp2 = ('localhost', 4000)


def run_communication ():
    try:
        while True:
            msg = input('Enter message to comp2: ')
            if msg == 'stop':
                break
            adr, port = comp2
            Client_HW.run_client(adr, port, msg)

            msg = input('Enter message to comp1: ')
            if msg == 'stop':
                break
            adr, port = comp1
            Client_HW.run_client(adr, port, msg)

    except KeyboardInterrupt:
        print('Communication between comp1 and comp2 has been stopped!')

def main():
    run_communication ()

if __name__ == '__main__':
    main()