import RPi.GPIO as G
from time import sleep
import spidev
#from gpiozero import MCP3008
#from pca9685_driver import Device
from HAL.i2c.pca9685 import PCA9685

spi = spidev.SpiDev()
driver = PCA9685(0x40)

def Init():
    print("Initialising")
    G.setmode(G.BCM)
    
    driver.write_to_register(driver.MODE1, 1)
    driver.write_to_register(driver.MODE2, 0)
    driver.write_to_register(driver.LEDX_YY_Z(0, 0, 1), 1<<4)
    driver.write_to_register(driver.LEDX_YY_Z(0, 1, 1), 0)
    driver.write_to_register(driver.LEDX_YY_Z(1, 0, 1), 1<<4)
    driver.write_to_register(driver.LEDX_YY_Z(1, 1, 1), 0)
    driver.write_to_register(driver.LEDX_YY_Z(2, 0, 1), 1<<4)
    driver.write_to_register(driver.LEDX_YY_Z(2, 1, 1), 0)
    
    driver.write_to_register(driver.LEDX_YY_Z(8, 0, 1), 1<<4)
    driver.write_to_register(driver.LEDX_YY_Z(8, 1, 1), 0)
    driver.write_to_register(driver.LEDX_YY_Z(9, 0, 1), 1<<4)
    driver.write_to_register(driver.LEDX_YY_Z(9, 1, 1), 0)

def BUTTONS_test():
    print("Testing Buttons")
    G.setup([5, 6], G.IN)
    G.setup([23, 24], G.OUT)
    while True:
        if G.input(5) == 0:
            print("5")
            G.output(24, 0)
        else:
            G.output(24, 1)

        if G.input(6) == 0:
            print("6")
            G.output(23, 0)
        else:
            G.output(23, 1)


def MOTOR_test():
    print("Testing motor driver")
    print("Testing Motordriver")
    G.setup([16,26,12,20,21,13], G.OUT)
    G.output([12,13], 1)
    print("M1")
    G.output(16,1)
    sleep(1)
    G.output(16,0)

    print("M2")
    G.output(26,1)
    sleep(1)
    G.output(26,0)

    print("M3")
    G.output(21,1)
    sleep(1)
    G.output(21,0)

    print("M4")
    G.output(20,1)
    sleep(1)
    G.output(20,0)

    G.output([12,13], 0)

def ADC_test(channel=0):
    spi.open(bus=0, device=0)
    spi.max_speed_hz = 50000
    to_send = [0x01, channel<<4, 0x55]
    G.setup(8, G.OUT)
    G.output(8, G.LOW)
    to_send = spi.xfer2(to_send)
    G.output(8, G.HIGH)
    spi.close()
    print(bin(to_send[1])+" "+bin(to_send[2]))
    return ((to_send[1]&0x03)<<8) + to_send[2]

def LED_test(N):
    print("Testing LEDs")
    for i in range(N): 
        driver.write_to_register(driver.LEDX_YY_Z(2, 1, 1), 1<<4)
        sleep(1)
        driver.write_to_register(driver.LEDX_YY_Z(2, 1, 1), 0)
        driver.write_to_register(driver.LEDX_YY_Z(1, 1, 1), 1<<4)
        sleep(1)
        driver.write_to_register(driver.LEDX_YY_Z(1, 1, 1), 0)
        driver.write_to_register(driver.LEDX_YY_Z(0, 1, 1), 1<<4)
        sleep(1)
        driver.write_to_register(driver.LEDX_YY_Z(0, 1, 1), 0)
        sleep(1)

try:
    Init()
    LED_test(2)
    print("Testing ADC")
    for N in range(8):    
        print("ADC CH" + str(N) + ": " + str(ADC_test(N)))
    MOTOR_test()
    BUTTONS_test()
except KeyboardInterrupt:
    driver.write_to_register(driver.LEDX_YY_Z(0, 1, 1), 0)
    driver.write_to_register(driver.LEDX_YY_Z(1, 1, 1), 0)
    driver.write_to_register(driver.LEDX_YY_Z(2, 1, 1), 0)
    print("quitting")
    exit()
