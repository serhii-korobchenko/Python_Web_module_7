import Server_HW_comp_threads
import Client_HW
from threading import Thread
from time import sleep

adress = 'localhost'
comp1 = 3000
comp2 = 4000


def run_communication():
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




if __name__ == '__main__':
   server1 = Thread(target=Server_HW_comp_threads.run_server, args=(comp1,))
   server2 = Thread(target=Server_HW_comp_threads.run_server, args=(comp2,))
   #client_activity = Thread(target=run_communication(), args=())
   server1.run()
   server2.run()
   #sleep(3)
   #client_activity.start()



