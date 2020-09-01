import serial
import threading
import time
import sys

print("Press CTRL+C to exit")
S = serial.Serial(port="/dev/ttyS0",baudrate="9600")
if not S.isOpen:
    S.open()

def reciever():
    while True:
        print(S.read().decode("utf-8"), end = '')

try:
    T = threading.Thread(target=reciever)
    T.start()

    while True:
        str = input() + '\n'
        #str = sys.stdin.read(1)
        S.write(str.encode("utf-8"))
        #print("Sending: " + str)



except:
    T.join()
    print("exitting")
    S.close()