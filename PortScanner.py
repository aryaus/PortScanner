import socket
import threading
from queue import Queue

# target defines your target for port scanning. Write your target ip hier
# do not use other people's network(illegal)
target = "127.0.0.1"
q = Queue()
open_ports_list = []

def portscan(p):
    try:
        s = socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, p))
        return True
    except:
        return False

# we use this function to fill the queue with the list of ports which we need
def q_range(list_port):
    for p in list_port:
        q.put(p)

# this function will print just the open ports and append it to the open ports list
def print_open_ports():
    while not q.empty():
        p = q.get()
        if portscan(p):
            print("Port {} is open".format(p))
            open_ports_list.append(p)

# we define a range for our list of ports
list_port = range(1,1024)
q_range(list_port)

thread_list = []

# in this loop we will define the range of threads
for th in range(100):
    thread = threading.Thread(target=print_open_ports)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print("open ports are:", open_ports_list)
