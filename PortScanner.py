import socket

# target defines your target for port scanning. this ip is your local host
# do not use other networks (illegal)
target = "127.0.0.1"

def portscan(p):
    try:
        s = socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(target, p)
        return True
    except:
        return False

print(portscan(25))
