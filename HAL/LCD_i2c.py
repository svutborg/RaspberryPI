from HAL.i2c.mcp23017 import mcp23017
from time import sleep

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


def __write(rs, data):
    global __mcp
    global __data_lat
    global __ctrl_lat
    global __rs
    global __e

    #lata = __mcp.read_register(__mcp.OLATA)
    clat = __mcp.read_register(__ctrl_lat)

    # The following is hardcoded doe to time constants:
    # RS A7, E A6, D0-7 D0-7

    # set RS
    if rs == 0:
        clat = clat & (~(1<<__rs))
    else:
        clat = clat | (1<<__rs)
    __mcp.write_register(__ctrl_lat, clat)

    # set data
    __mcp.write_register(__data_lat, data)

    # Toggle enable
    clat = clat | (1<<__e)
    __mcp.write_register(__ctrl_lat, clat)
    sleep(0.000001)  # wait 1 us
    clat = clat & (~(1<<__e))
    __mcp.write_register(__ctrl_lat, clat)


def __write_command(cmd):
    __write(0, cmd)


def __write_data(data):
    __write(1, data)

def init_display(rs, e, d, n_lines=0, font=0, line_addresses = [0, 46, 20, 84], i2c_address = 0x20):
    global __rs
    global __e
    global __mcp
    global __line_addresses
    global __ctrl_lat 
    global __data_lat

    __line_addresses = line_addresses

    __mcp = mcp23017(i2c_address)
    if rs in PORTA and e in PORTA:
        __ctrl_lat = __mcp.OLATA
        __data_lat = __mcp.OLATB
        __rs = rs
        __e = e
    elif rs in PORTB and e in PORTB:
        __ctrl_lat = __mcp.OLATB
        __data_lat = __mcp.OLATA
        __rs = rs-8
        __e = e-8
    else:
        raise AttributeError("Both rs and e must be in etiher PORTA or PORTB")

    # define pins as outputs
    iodir = 0x0000
    for pin in d:
        iodir |= 1<<pin
    iodir |= 1<<rs
    iodir |= 1<<e
    iodir = ~iodir
    __mcp.write_register(__mcp.IODIRA, iodir & 0x00FF)
    __mcp.write_register(__mcp.IODIRB, (iodir>>8) & 0x00FF)

    # set enable low
    clat = __mcp.read_register(__ctrl_lat)
    clat = clat & (~(1<<__e))
    __mcp.write_register(__ctrl_lat, clat)

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


def write_char(c):
    __write_data(ord(c))


def write_string(s):
    for c in s:
        write_char(c)


def set_cursor_pos(row, col):
    global __line_addresses
    
    set_ddram_address(__line_addresses[row] + col)


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
