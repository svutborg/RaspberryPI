import RPi.GPIO as G
from time import sleep
from HAL import leddriver
from gpiozero import MCP3008

print("Testing LEDs")
L = leddriver.LEDDriver()
L.LED_on("LD1")
sleep(0.5)
L.LED_off("LD1")
L.LED_on("LD2")
sleep(0.5)
L.LED_off("LD2")
L.LED_on("LD3")
sleep(0.5)
L.LED_off("LD3")
L.LED_on("LD4")
sleep(0.5)
L.LED_off("LD4")
L.LED_on("LD5")
sleep(0.5)
L.LED_off("LD5")
L.LED_on("LDR")
sleep(0.5)
L.LED_off("LDR")
L.LED_on("LDG")
sleep(0.5)
L.LED_off("LDG")
L.LED_on("LDB")
sleep(0.5)
L.LED_off("LDB")

print("Testing Motordriver")
G.setmode(G.BCM)
G.setup([16,26,12,20,21,13], G.OUT)
G.output([12,13], 1)
G.output(16,1)
sleep(0.5)
G.output(16,0)

G.output(26,1)
sleep(0.5)
G.output(26,0)

G.output(21,1)
sleep(0.5)
G.output(21,0)

G.output(20,1)
sleep(0.5)
G.output(20,0)

print("Testing ADC")
adc = MCP3008(device=1, channel=0)
print(adc.value)
adc = MCP3008(device=1, channel=1)
print(adc.value)
adc = MCP3008(device=1, channel=2)
print(adc.value)
adc = MCP3008(device=1, channel=3)
print(adc.value)
adc = MCP3008(device=1, channel=4)
print(adc.value)
adc = MCP3008(device=1, channel=5)
print(adc.value)
adc = MCP3008(device=1, channel=6)
print(adc.value)
adc = MCP3008(device=1, channel=7)
print(adc.value)

print("Testing D-pad")
directions = {
    "up": 27,
    "down": 24,
    "left": 23,
    "right": 17,
    "push": 22
}
G.setmode(G.BCM)
for dir in directions:
    print(dir)
    G.setup(directions[dir], G.IN)
    while True:
        if G.input(directions[dir]) == 1:
            break



