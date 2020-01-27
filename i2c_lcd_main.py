import HAL.LCD_i2c as LCD
import time

LCD.init_display()

while True:
    LCD.write_string(input())

