import smbus
from time import sleep

DEVICE_BUS = 1

DEVICE_ADDR = 0b0100000 # [0 1 0 0 A2 A1 A0]

IODIRB = 0x01
GPIOB = 0x13
OLATB = 0x15

bus = smbus.SMBus(DEVICE_BUS)
bus.write_byte_data(DEVICE_ADDR, IODIRB, ~(1<<6))



while True:
    for i in range(1):
#        print("{0}".format((bus.read_byte_data(DEVICE_ADDR,GPIOB)>>5)&1)
        val = bus.read_byte_data(DEVICE_ADDR, GPIOB)
        print(val)
        print(val>>5)
        print((val>>5)&1)
        sleep(0.5)
        
    state = not ((bus.read_byte_data(DEVICE_ADDR, OLATB)>>6)&1)
    print("State: " + str(state))
    bus.write_byte_data(DEVICE_ADDR, OLATB, state<<6)
    

