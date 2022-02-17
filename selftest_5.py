import RPi.GPIO as G
from time import sleep, time
import spidev
from pca9632.controller import Controller
from itertools import chain

def init():
  print("Initialising")
  global led, spi
  G.setmode(G.BCM)
  G.setup([5, 6], G.IN)
  G.setup([23, 24], G.OUT)
	
  spi = spidev.SpiDev()
  spi.open(bus=0, device=0)
  spi.max_speed_hz = 50000
  try:
    led = Controller()
    led.all_off()
  except OSError:
    print("I2C is not working")


def buttons_test():
  print("Testing Buttons")
  BTN1=False 
  BTN2=False
  t = int(time())+10
	
  while (not BTN1) or (not BTN2):
    if G.input(5) and not BTN1:
      print("BTN1 pressed")
      G.output(23, 1)										 
      BTN1 = True
    if G.input(6) and not BTN2:
      print("BTN2 pressed")
      G.output(24, 1)										 
      BTN2 = True
    if int(time()) > t:
      print("Timeout: No buttons pressed") 
      break	 
	
  sleep(2)
  G.output(23, 0)
  G.output(24, 0)
	

def motor_test():
  print("Testing motor driver")
  G.setup([16, 26, 12, 20, 21, 13], G.OUT)
  G.output([12, 13], 1)
  print("M1")
  G.output(16, 1)
  sleep(1)
  G.output(16, 0)

  print("M2")
  G.output(20, 1)
  sleep(1)    
  G.output(20, 0)

  print("M3")
  G.output(26, 1)
  sleep(1)
  G.output(26, 0)

  print("M4")
  G.output(21, 1)
  sleep(1)
  G.output(21, 0)

  G.output([12, 13], 0)


def adc_read(channel=0):
  to_send = [0x01, 0x80 | channel<<4, 0x55]
  to_send = spi.xfer2(to_send)
  return ((to_send[1]&0x03)<<8) + to_send[2]


def adc_test():
  print("Testing ADC")
  for N in range(8):
    print("ADC CH" + str(N) + ": " + str(adc_read(channel=N)))
							 

def led_test(n):
  print("Testing LEDs")
  G.output(23, 1)	
  G.output(24, 1)	
  sleep(1)
  for i in range(n):
    for j in range(3):
      for k in chain(range(256), range(255, -1, -1)):
        led.set_led(j+1, k)
        sleep(0.001)
  led.all_off()
  G.output(23, 0)	
  G.output(24, 0)	

if __name__ == "__main__":
	try:
	  init()
	  try:
	    led_test(1)
	  except OSError:
	    pass
	  except NameError:
	    pass
	  adc_test()
	  motor_test()
	  buttons_test()
	except KeyboardInterrupt:
	  spi.close()
	  led.all_off()
	  print("quitting")
	  exit()
