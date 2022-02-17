import HAL.LCD_i2c as LCD
import time

LCD.init_display(rs=LCD.A7, e=LCD.A5)

while True:
    LCD.write_string(input())
#    time.sleep(0.2)
