import smbus
from time import sleep

class mcp23017:

    IODIRA =   0x00
    IODIRB =   0x01
    IPOLA =    0x02
    IPOLB =    0x03
    GPINTENA = 0x04
    GPINTENB = 0x05
    DEFVALA =  0x06
    DEFVALB =  0x07
    INTCONA =  0x08
    INTCONB =  0x09
    IOCONA =   0x0A
    IOCONB =   0x0B
    GPPUA =    0x0C
    GPPUB =    0x0D
    INTFA =    0x0E
    INTFB =    0x0F
    INTCAPA =  0x10
    INTCAPB =  0x11
    GPIOA =    0x12
    GPIOB =    0x13
    OLATA =    0x14
    OLATB =    0x15

    def __init__(self, address=0):
        self.address = 0b0100000 & address # [0 1 0 0 A2 A1 A0]
        self.bus = smbus.SMBus(1)

    def write_register(self, register, data):
        self.bus.write_byte_data(self.address, register, data)




'''
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


'''
