if __name__ == "__main__":
	from i2c import pca9685
	import time
else:
	from HAL.i2c import pca9685
import math


class ServoDriver:
	def __init__(self):
		self.controller = pca9685.PCA9685(0x40, pca9685.PCA9685.TOTEMPOLE, 50)

	def set_pulse_width(self, width, led):
		try:
			assert 1 <= width <= 2  # Check that the pulse width is between 1 and 2 ms
			assert 10 <= led <= 15  # Check that led nr is correct range for servo pins

			on = math.floor(width*4096/20)
			print(on)

			self.controller.write_to_register(self.controller.LEDX_YY_Z(led, 0, 0), 0)
			self.controller.write_to_register(self.controller.LEDX_YY_Z(led, 0, 1), 0)
			self.controller.write_to_register(self.controller.LEDX_YY_Z(led, 1, 0), on)
			self.controller.write_to_register(self.controller.LEDX_YY_Z(led, 1, 1), on >> 8)
		except AssertionError:
			raise ValueError


if __name__ == "__main__":
	L = ServoDriver()
	L.set_pulse_width(2, 10)
	print("done")