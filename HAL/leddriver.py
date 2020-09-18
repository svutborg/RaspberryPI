if __name__ == "__main__":
  from i2c import pca9685
  import time
else:
  from HAL.i2c import pca9685

class LEDDriver:
  def __init__(self, intensity=5):
    self.LED_intensity(intensity)
    self.controller = pca9685.PCA9685(0x40)
    self.controller.write_to_register(self.controller.MODE1, 1)
    self.controller.write_to_register(self.controller.MODE2, 0)
    
    self.LED_OFF()
  
  def LED_OFF(self):
    self.controller.write_to_register(self.controller.LEDX_YY_Z(0, 0, 1), 1<<4)
    self.controller.write_to_register(self.controller.LEDX_YY_Z(0, 1, 1), 0)
    self.controller.write_to_register(self.controller.LEDX_YY_Z(1, 0, 1), 1<<4)
    self.controller.write_to_register(self.controller.LEDX_YY_Z(1, 1, 1), 0)
    self.controller.write_to_register(self.controller.LEDX_YY_Z(2, 0, 1), 1<<4)
    self.controller.write_to_register(self.controller.LEDX_YY_Z(2, 1, 1), 0)
  
  def LED_ON(self):
    self._set_duty((255>>3)*self.intensity, 2)
    self._set_duty((255>>3)*self.intensity, 1)
    self._set_duty((255>>3)*self.intensity, 0)
  
  def LED_RGB(self, r, g, b):
    assert 0x00 <= r <= 0xFF 
    assert 0x00 <= g <= 0xFF 
    assert 0x00 <= b <= 0xFF
    
    self._set_duty((r>>3)*self.intensity, 2)
    self._set_duty((g>>3)*self.intensity, 1)
    self._set_duty((b>>3)*self.intensity, 0)
  
  def LED_intensity(self, i):
    self.intensity = int(i*1.28)

  def _set_duty(self, duty, diode):
    assert diode in range(3)
    assert 0 <= duty <= 0x0fff
    duty_ = 0x0fff - duty
    
    self.controller.write_to_register(self.controller.LEDX_YY_Z(diode, 0, 1), (duty  >> 8)  & 0x0f)
    self.controller.write_to_register(self.controller.LEDX_YY_Z(diode, 1, 1), (duty_ >> 8)  & 0x0f)
    self.controller.write_to_register(self.controller.LEDX_YY_Z(diode, 0, 0), duty  & 0x00ff)
    self.controller.write_to_register(self.controller.LEDX_YY_Z(diode, 1, 0), duty_ & 0x00ff)
  
if __name__ == "__main__":
  L = LEDDriver()
  L.LED_ON()
  time.sleep(1)
  L.LED_RGB(120, 0, 120)
  time.sleep(1)
  L.LED_OFF()