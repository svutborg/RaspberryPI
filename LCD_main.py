from time import sleep
import LCD

LCD.init_display(4, 17, [27, 22, 10, 9, 11, 5, 6, 13], 1, 0)
#LCD.init_display(21, 20, [13, 16, 19, 26], 0, 0)
for i in range(100):
    c = chr(ord('0')+i)
    LCD.set_cursor_pos(i // 16, i % 16)
    LCD.write_char(c)
    print(c)
#LCD.write_string("Hello world!")
    sleep(0.5)
sleep(1)
LCD.clear_display()
