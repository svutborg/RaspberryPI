#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 12:24:12 2019

@author: svu
"""
import time
from i2c import leddriver
import RPi.GPIO as GPIO
import sys
import spidev

GPIO.setwarnings(False)
testparameters = "all"

if len(sys.argv) > 1:
    testparameters = sys.argv[1]
    if testparameters not in ["all", "led", "dpad", "adc", "motor"]:
        print("Error, non-valid input parameter")
        print("Valid commands: all, led, dpad, adc")
        sys.exit()

#LED test
if testparameters == "all" or testparameters == "led":
    print("Testing LEDS")
    d = leddriver.LEDDriver()
    for led in d.LEDS.keys():
        d.LED_on(led)
        time.sleep(0.5)
        d.LED_off(led)    
    time.sleep(1)

#dpad test
if testparameters == "all" or testparameters == "dpad":
    print("Testing DPAD")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup([17, 27, 22, 23, 24], GPIO.IN)
    timeout = time.time() + 10
    working = [False, False, False, False, False]
    while True:
        if GPIO.input(17) and (not working[0]):
            print("D")
            working[0] = True
        if GPIO.input(27) and (not working[1]):
            print("B")
            working[1] = True
        if GPIO.input(22) and (not working[2]):
            print("PUSH")
            working[2] = True
        if GPIO.input(23) and (not working[3]):
            print("A")
            working[3] = True
        if GPIO.input(24) and (not working[4]):
            print("C")
            working[4] = True
        if all(working):
            print("Dpad test passed!")
            break
        if time.time() > timeout:
            print("Test timed out")
            break

#ADC test    
if testparameters == "all" or testparameters == "adc":
    print("Testing ADC")
    adc = spidev.SpiDev()
    adc.open(bus=0,device=1)
    adc.max_speed_hz = 100000
    for ch in range(8):
        data = [0x01, 0x80|ch<<4, 0x00]
        voltage = adc.xfer2(data)
        voltage = ((0x03&voltage[1])<<8)|voltage[2]
        voltage = (voltage*5)/1024
        print("Channel " + str(ch) + ": " + "{:.2f}".format(voltage) + "V")
    
#motor driver test
if testparameters == "all" or testparameters == "motor":
    print("Testing motordriver")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup([13, 12, 26, 16, 20, 21], GPIO.OUT)
    GPIO.output([13, 12], GPIO.HIGH)

    GPIO.output([16], GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output([16], GPIO.LOW)
    
    GPIO.output([26], GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output([26], GPIO.LOW)

    GPIO.output([21], GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output([21], GPIO.LOW)

    GPIO.output([20], GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output([20], GPIO.LOW)

    GPIO.output([16], GPIO.HIGH)
    GPIO.output([26], GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output([16], GPIO.LOW)
    GPIO.output([26], GPIO.LOW)

    GPIO.output([20], GPIO.HIGH)
    GPIO.output([21], GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output([20], GPIO.LOW)
    GPIO.output([21], GPIO.LOW)

    GPIO.output([16], GPIO.HIGH)
    GPIO.output([26], GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output([16], GPIO.LOW)
    GPIO.output([26], GPIO.LOW)

    GPIO.output([20], GPIO.HIGH)
    GPIO.output([21], GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output([20], GPIO.LOW)
    GPIO.output([21], GPIO.LOW)
    
    GPIO.output([13, 12], GPIO.LOW)
    
    
    
    
    
    