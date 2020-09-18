import RPi.GPIO as G
from time import sleep
import spidev
from HAL import leddriver
from itertools import chain

spi = spidev.SpiDev()
led = leddriver.LEDDriver()


def init():
    print("Initialising")
    G.setmode(G.BCM)

    led.LED_OFF()


def buttons_test():
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


def motor_test():
    print("Testing motor driver")
    G.setup([16, 26, 12, 20, 21, 13], G.OUT)
    G.output([12, 13], 1)
    print("M1")
    G.output(16, 1)
    sleep(1)
    G.output(16, 0)

    print("M2")
    G.output(26, 1)
    sleep(1)
    G.output(26, 0)

    print("M3")
    G.output(21, 1)
    sleep(1)
    G.output(21, 0)

    print("M4")
    G.output(20, 1)
    sleep(1)
    G.output(20, 0)

    G.output([12, 13], 0)


def adc_test(channel=0):
    spi.open(bus=0, device=0)
    spi.max_speed_hz = 50000
    to_send = [0x01, channel << 4, 0x55]
    G.setup(8, G.OUT)
    G.output(8, G.LOW)
    to_send = spi.xfer2(to_send)
    G.output(8, G.HIGH)
    spi.close()
    return ((to_send[1] & 0x03) << 8) + to_send[2]


def led_test(n):
    print("Testing LEDs")
    for i in range(n):
        for j in range(3):
            for k in chain(range(256), range(255, -1, -1)):
                led.LED_RGB(k if j == 0 else 0, k if j == 1 else 0, k if j == 2 else 0)
                sleep(0.001)
    led.LED_OFF()


try:
    init()
    led_test(1)
    print("Testing ADC")
    for N in range(8):
        print("ADC CH" + str(N) + ": " + str(adc_test(N)))
    motor_test()
    buttons_test()
except KeyboardInterrupt:
    led.LED_OFF()
    print("quitting")
    exit()
