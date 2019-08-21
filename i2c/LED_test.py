#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 12:45:09 2019

@author: pi
"""
import LEDDriver
import time

d = LEDDriver.LEDDriver()

for i in d.LEDS.keys():
    d.LED_on(i)
    time.sleep(0.5)
for i in d.LEDS.keys():
    d.LED_off(i)
    time.sleep(0.5)
    
print('test completed')