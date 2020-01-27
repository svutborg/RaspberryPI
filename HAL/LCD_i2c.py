from HAL.i2c.mcp23017 import mcp23017
from time import sleep
#import HAL.i2c.mcp23017.mcp23017 as mcp23017
A0 = 0x00
A1 = 0x01
A2 = 0x02
A3 = 0x03
A4 = 0x04
A5 = 0x05
A6 = 0x06
A7 = 0x07

PORTA = [A0, A1, A2, A3, A4, A5, A6, A7]

B0 = 0x08
B1 = 0x09
B2 = 0x0A
B3 = 0x0B
B4 = 0x0C
B5 = 0x0D
B6 = 0x0E
B7 = 0x0F

PORTB = [B0, B1, B2, B3, B4, B5, B6, B7]

__rs = 0
__e = 0
__d = []
__mode = 0
__lines = 0

def __write(rs, data):
    global __mcp

    lata = __mcp.read_register(mcp23017.OLATA)

    # The following is hardcoded doe to time constants:
    # RS A7, E A6, D0-7 D0-7

    # set RS
    if rs == 0:
        lata = lata & (~(1<<7))
    else:
        lata = lata | (1<<7)
    __mcp.write_register(mcp23017.OLATA, lata)

    # set data
    __mcp.write_register(mcp23017.OLATB, data)

    # Toggle enable
    lata = lata | (1<<6)
    __mcp.write_register(mcp23017.OLATA, lata)
    sleep(0.000001)  # wait 1 us
    lata = lata & (~(1<<6))
    __mcp.write_register(mcp23017.OLATA, lata)


def __write_command(cmd):
    __write(0, cmd)


def __write_data(data):
    __write(1, data)

def init_display(rs=A7, e=A6, d=PORTB, n_lines=0, font=0):
    global __rs
    global __e
    global __d
    global __mode
    global __lines
    global __mcp

    __rs = rs
    __e = e
    __d = d
    __lines = n_lines

    __mcp = mcp23017()

    # The following is hardcoded doe to time constants:
    # RS A7, E A6, D0-7 D0-7

    # define pins as outputs
    __mcp.write_register(mcp23017.IODIRB, 0x00)
    __mcp.write_register(mcp23017.IODIRA, 0x3F)

    # set enable low
    lata = __mcp.read_register(mcp23017.OLATA)
    lata = lata & (~(1<<6))
    __mcp.write_register(mcp23017.OLATA, lata)

    # run init sequence
    function_set(1, 0, 0)
    sleep(0.005)  # wait 5 ms
    function_set(1, 0, 0)
    sleep(0.0005)  # wait 500 us
    function_set(1, 0, 0)

    function_set(1, n_lines, font)
    display_on_off(0, 1, 1)
    clear_display()
    entry_mode_set(1, 0)

    display_on_off(1, 1, 1)
    '''
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
        '''

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
