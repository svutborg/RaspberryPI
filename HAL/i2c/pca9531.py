import smbus

class PCA9531:
    INPUT_r = 0x00
    PSC0_r = 0x01
    PWM0_r = 0x02
    PSC1_r = 0x03
    PWM1_r = 0x04
    LS0_r  = 0x05
    LS1_r  = 0x06

    def __init__(self, deviceAddress):
        try:
            assert 0x60 <= deviceAddress <= 0x67
            self.deviceAddress = deviceAddress
        except AssertionError:
            raise ValueError
        self.bus = smbus.SMBus(1)

    def write_to_register(self, register, data):
        self.bus.write_byte_data(self.deviceAddress, register, data)

    def read_from_register(self, register):
        return self.bus.read_byte_data(self.deviceAddress, register)
