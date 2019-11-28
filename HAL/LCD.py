import RPi.GPIO as GPIO
from time import sleep

__rs = 0
__e = 0
__d = []
__mode = 0
__lines = 0


def __write(rs, data):
    global __mode
    GPIO.output(__rs, rs)

    if __mode == 4:     # Only clock if
        msn = data >> 4  # Most Significant Nibble
        lsn = data & 0x0F  # Least Significant Nibble

        for i in __d:
            GPIO.output(i, msn & 1)
            msn = msn >> 1

        GPIO.output(__e, GPIO.HIGH)
        sleep(0.000001)  # wait 1 us
        GPIO.output(__e, GPIO.LOW)

        for i in __d:
            GPIO.output(i, lsn & 1)
            lsn = lsn >> 1
    else:
        for i in __d:
            GPIO.output(i, data & 1)
            data = data >> 1

    GPIO.output(__e, GPIO.HIGH)
    sleep(0.000001)  # wait 1 us
    GPIO.output(__e, GPIO.LOW)


def __write_command(cmd):
    __write(0, cmd)


def __write_data(data):
    __write(1, data)


def init_display(rs_bcm, e_bcm, d_bcm, n_lines, font):
    global __rs
    global __e
    global __d
    global __mode
    global __lines

    GPIO.setmode(GPIO.BCM)
    __rs = rs_bcm  # type: int
    __e = e_bcm  # type: int
    __d = d_bcm  # type: [int]
    __lines = n_lines
    GPIO.setup(rs_bcm, GPIO.OUT)
    GPIO.setup(e_bcm, GPIO.OUT)
    GPIO.setup(e_bcm, GPIO.LOW)
    for i in d_bcm:
        GPIO.setup(i, GPIO.OUT)

    function_set(1, 0, 0)
    sleep(0.005)  # wait 5 ms
    function_set(1, 0, 0)
    sleep(0.0005)  # wait 500 us
    function_set(1, 0, 0)

    if len(d_bcm) == 8:  # Auto set mode from number of data pins provided
        __mode = 8
        function_set(1, n_lines, font)
        display_on_off(0, 1, 1)
        clear_display()
        entry_mode_set(1, 0)
    else:
        __mode = 4
        function_set(0, n_lines, font)
        display_on_off(0, 1, 1)
        clear_display()
        entry_mode_set(1, 0)

    display_on_off(1, 1, 1)


def write_char(c):
    __write_data(ord(c))


def write_string(s):
    for c in s:
        write_char(c)


def set_cursor_pos(row, col):
    global __lines
    if __lines == 0:
        if row == 0:
            set_ddram_address(col)
        elif row == 1:
            set_ddram_address(col+40)
    elif __lines == 1:
        if row == 0:
            set_ddram_address(col)
        elif row == 1:
            set_ddram_address(col+64)
        elif row == 2:
            set_ddram_address(col+16)
        elif row == 3:
            set_ddram_address(col+80)


def clear_display():
    __write_command(0x01)
    sleep(0.002)


def return_home():
    __write_command(0x02)
    sleep(0.002)


def entry_mode_set(i_d, sh):
    __write_command(0x04 | (i_d & 1) << 1 | (sh & 1))
    sleep(0.00004)


def display_on_off(d, c, b):
    __write_command(0x08 | (d & 1) << 2 | (c & 1) << 1 | (b & 1))
    sleep(0.00004)


def cursor_display_shift(sc, rl):
    __write_command(0x10 | (sc & 1) << 3 | (rl & 1) << 2)
    sleep(0.00004)


def function_set(dl, n, f):
    __write_command(0x20 | (dl & 1) << 4 | (n & 1) << 3 | (f & 1) << 2)
    sleep(0.00004)


def set_ddram_address(add):
    __write_command(0x80 | add)
