import smbus
import math

class PCA9685:
	MODE1 =         0x00
	MODE2 =         0x01
	SUBADR1 =       0x02
	SUBADR2 =       0x03
	SUBADR3 =       0x04
	ALLCALLADR =    0x05

	OPENDRAIN = 0
	TOTEMPOLE = 1

	# X    LED number
	# YY   ON: 0, OFF: 1
	# Z    L: 0, H: 1
	def LEDX_YY_Z(self, X, YY, Z):
		return 0x06+(X << 2 | YY << 1 | Z)

	def __init__(self, device_address, out_drv=OPENDRAIN, frequency=50):
		try:
			assert 0x40 <= device_address <= 0x7F
			self.deviceAddress = device_address
			self.bus = smbus.SMBus(1)
			self.write_to_register(self.MODE1, 1 << 4)
			pre = math.floor(25000000/(4096*frequency)-1)
			assert 3 <= pre <= 255
			self.write_to_register(0xFE, pre)  # set prescaler for 50 Hz round((osc_clk)/(4096*50))-1 -> 121
			self.write_to_register(self.MODE1, 1)
			self.write_to_register(self.MODE2, 0 | out_drv << 2)
		except AssertionError:
			raise ValueError

	def write_to_register(self, register, data):
		self.bus.write_byte_data(self.deviceAddress, register, data)

	def read_from_register(self, register):
		return self.bus.read_byte_data(self.deviceAddress, register)
