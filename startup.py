from HAL.i2c.pca9685 import PCA9685
from HAL import leddriver
from time import sleep

driver = PCA9685(0x40)
led = leddriver.LEDDriver()


def set_floating(pin):
	driver.write_to_register(driver.LEDX_YY_Z(pin, 0, 1), 1<<4)
	driver.write_to_register(driver.LEDX_YY_Z(pin, 1, 1), 0)


driver.write_to_register(driver.MODE1, 1)
driver.write_to_register(driver.MODE2, 0)
for p in range(16):
	set_floating(p)

led.led_rgb(100, 0, 0)
sleep(0.2)
led.led_rgb(0, 100, 0)
sleep(0.2)
led.led_rgb(0, 0, 100)
sleep(0.2)
led.led_off()
