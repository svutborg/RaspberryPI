from smbus2 import SMBus
from time import sleep
from ctypes import Union, Structure, c_uint

class Register_bits(Structure):
    _fields_ = [
            ("bit0", c_uint, 1),
            ("bit1", c_uint, 1),
            ("bit2", c_uint, 1),
            ("bit3", c_uint, 1),
            ("bit4", c_uint, 1),
            ("bit5", c_uint, 1),
            ("bit6", c_uint, 1),
            ("bit7", c_uint, 1),
        ]

class Register_value(Union):
    _fields_ = [
            ("byte", c_uint),
            ("bits", Register_bits)
        ]

class Register():
    
    def __init__(self, name: str, address: int, default_value: int = 0):
        self.name = name
        self.address = address
        self.default_value = default_value
        self.value = Register_value(default_value)
    
    def reset(self):
        self.value = Register_value(self.default_value)

class mcp23017:
    
    register_addresses = { # first address is with IOCON.BANK = 0 
        "IODIRA":   [0x00, 0x00],
        "IPOLA":    [0x02, 0x01],
        "GPINTENA": [0x04, 0x02],
        "DEFVALA":  [0x06, 0x03],
        "INTCONA":  [0x08, 0x04],
        "IOCONA":   [0x0A, 0x05],
        "GPPUA":    [0x0C, 0x06],
        "INTFA":    [0x0E, 0x07],
        "INTCAPA":  [0x10, 0x08],
        "GPIOA":    [0x12, 0x09],
        "OLATA":    [0x14, 0x0A],

        "IODIRB":   [0x01, 0x10],
        "IPOLB":    [0x03, 0x11],
        "GPINTENB": [0x05, 0x12],
        "DEFVALB":  [0x07, 0x13],
        "INTCONB":  [0x09, 0x14],
        "IOCONB":   [0x0B, 0x15],
        "GPPUB":    [0x0C, 0x16],
        "INTFB":    [0x0E, 0x17],
        "INTCAPB":  [0x11, 0x18],
        "GPIOB":    [0x13, 0x19],
        "OLATB":    [0x15, 0x1A]
    }

    def __init__(self, address=0, bank=0):
        self.address = 0b0100000 | address # [0 1 0 0 A2 A1 A0]
        self.bus = SMBus(1)
        for r in mcp23017.register_addresses:
            setattr(self, r, Register(r, mcp23017.register_addresses[r][bank], 0xff if "IODIR" in r else 0x00))

    def write_register(self, register, data):
        self.bus.write_byte_data(self.address, register.address, data)

    def read_register(self, register):
        return self.bus.read_byte_data(self.address, register.address)

if __name__ == "__main__":
    print("Testing mcp23017 lib")
    dev = mcp23017()
    print(dev.IODIRA.value.byte)
    print(dev.GPIOA.value.byte)
    #print(dev.IODIRA.value.byte)
