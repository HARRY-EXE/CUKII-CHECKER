import platform
import os
import socket

global arc

print(f' •\x1b[38;5;196m ->\x1b[37m CHECKING FOR UPDATES ')
os.system('git pull --quiet')

def check_internet():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        return False
if check_internet():
    pass
else:
    exit("•\x1b[38;5;196m ->\x1b[37m NO INTERNET CONNECTION")
        
def check_python_architecture():
    global arc
    architecture = platform.architecture()
    if architecture[0] == '32bit':
        arc = "32BIT"
        print(f' •\x1b[38;5;196m ->\x1b[37m 32BIT DETECTED')
        exit("•\x1b[38;5;196m ->\x1b[37m UNSUPPORTED DEVICE TYPE")
    elif architecture[0] == '64bit':
        arc = "64BIT"
        print(f' •\x1b[38;5;196m ->\x1b[37m 64BIT DETECTED')
        print(f' •\x1b[38;5;196m ->\x1b[37m STARTING CUKII-CHECKER ')
        import data.HARRY64
        data.HARRY64
    else:
        arc = "INVALID"
        exit("•\x1b[38;5;196m ->\x1b[37m UNKNOWN DEVICE TYPE")


if __name__ == "__main__":
    check_internet()
    check_python_architecture()
