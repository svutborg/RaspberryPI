import smbus

class PCA9685:
    MODE1 =         0x00
    MODE2 =         0x01
    SUBADR1 =       0x02
    SUBADR2 =       0x03
    SUBADR3 =       0x04
    ALLCALLADR =    0x05

    # X    LED number
    # YY   ON: 0, OFF: 1
    # Z    L: 0, H: 1
    def LEDX_YY_Z(self, X, YY, Z):
        return 0x06+(X<<2|YY<<1|Z)

    def __init__(self, deviceAddress):
        try:
            assert 0x40 <= deviceAddress <= 0x7F
            self.deviceAddress = deviceAddress
        except AssertionError:
            raise ValueError
        self.bus = smbus.SMBus(1)

    def write_to_register(self, register, data):
        #print("Writing: "+hex(data)+" to: "+hex(register))
        self.bus.write_byte_data(self.deviceAddress, register, data)

    def read_from_register(self, register):
        return self.bus.read_byte_data(self.deviceAddress, register)
