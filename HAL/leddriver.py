if __name__ == "__main__":
	from i2c import pca9685
	import time
else:
	from HAL.i2c import pca9685


class LEDDriver:
	intensity = 0

	def __init__(self, intensity=5):
		self.led_intensity(intensity)
		self.controller = pca9685.PCA9685(0x40, pca9685.PCA9685.OPENDRAIN)

		self.led_off()

	def led_off(self):
		for i in range(3):
			self.controller.write_to_register(self.controller.LEDX_YY_Z(i, 0, 1), 1 << 4)
			self.controller.write_to_register(self.controller.LEDX_YY_Z(i, 1, 1), 0)

	def led_on(self):
		self._set_duty((255 >> 3)*self.intensity, 2)
		self._set_duty((255 >> 3)*self.intensity, 1)
		self._set_duty((255 >> 3)*self.intensity, 0)

	def led_rgb(self, r, g, b):
		assert 0x00 <= r <= 0xFF
		assert 0x00 <= g <= 0xFF
		assert 0x00 <= b <= 0xFF

		self._set_duty((r >> 3)*self.intensity, 2)
		self._set_duty((g >> 3)*self.intensity, 1)
		self._set_duty((b >> 3)*self.intensity, 0)

	def led_intensity(self, i):
		self.intensity = int(i*1.28)

	def _set_duty(self, duty, diode):
		assert diode in range(3)
		assert 0 <= duty <= 0x0fff
		duty_ = 0x0fff - duty

		self.controller.write_to_register(self.controller.LEDX_YY_Z(diode, 0, 1), (duty >> 8) & 0x0f)
		self.controller.write_to_register(self.controller.LEDX_YY_Z(diode, 1, 1), (duty_ >> 8) & 0x0f)
		self.controller.write_to_register(self.controller.LEDX_YY_Z(diode, 0, 0), duty & 0x00ff)
		self.controller.write_to_register(self.controller.LEDX_YY_Z(diode, 1, 0), duty_ & 0x00ff)


if __name__ == "__main__":
	L = LEDDriver()
	L.led_on()
	time.sleep(1)
	L.led_rgb(120, 0, 120)
	time.sleep(1)
	L.led_off()