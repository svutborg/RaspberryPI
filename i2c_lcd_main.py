import HAL.LCD_i2c as LCD
import time

LCD.init_display(rs=LCD.B7, e=LCD.B5, d=LCD.PORTA, n_lines=1, i2c_address=0x20)
#LCD.init_display(rs=LCD.A7, e=LCD.A5, d=LCD.PORTB, n_lines=1, i2c_address=0x21)

while (s := input()) != "": # Repeat while the input string is not empty
    LCD.write_string(s)

LCD.clear_display()
LCD.set_cursor_pos(0,0)
LCD.write_string("1")
LCD.set_cursor_pos(1,0)
LCD.write_string("2")
LCD.set_cursor_pos(2,0)
LCD.write_string("3")
LCD.set_cursor_pos(3,0)
LCD.write_string("4")
