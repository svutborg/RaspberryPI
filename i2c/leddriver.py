from myLib.i2c.pca9531 import PCA9531
import collections

class LEDDriver:
    LEDS = collections.OrderedDict([
            ("LD1", 0),
            ("LD2", 2),
            ("LD3", 4),
            ("LD4", 6),
            ("LD5", 0),
            ("LDR", 2),
            ("LDG", 4),
            ("LDB", 6),
    ])  

    def __init__(self):
        self.controller = PCA9531.PCA9531(0x60)
        self.LS0_State = self.controller.read_from_register(self.controller.LS0_r)
        self.LS1_State = self.controller.read_from_register(self.controller.LS1_r)
	
    def LED_on(self, led):
        if led in list(self.LEDS.keys())[0:4]:
            self.LS0_State = 0x01<<self.LEDS[led] | self.LS0_State
            self.controller.write_to_register(self.controller.LS0_r, self.LS0_State)
        else:
            self.LS1_State = 0x01<<self.LEDS[led] | self.LS1_State
            self.controller.write_to_register(self.controller.LS1_r, self.LS1_State)

    def LED_off(self, led):
        if led in list(self.LEDS.keys())[0:4]:
            self.LS0_State = (~(0x03<<self.LEDS[led])) & self.LS0_State
            self.controller.write_to_register(self.controller.LS0_r, self.LS0_State)
        else:
            self.LS1_State = (~(0x03<<self.LEDS[led])) & self.LS1_State
            self.controller.write_to_register(self.controller.LS1_r, self.LS1_State)

if __name__ == "__main__":
    L = LEDDriver()
    L.LED_on("LD3")
    print("LED3 on")