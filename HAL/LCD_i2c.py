import HAL.i2c.mcp23017 as mcp23017
A0 = 0x08
A1 = 0x09
A2 = 0x0A
A3 = 0x0B
A4 = 0x0C
A5 = 0x0D
A6 = 0x0E
A7 = 0x0F

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

def init_display(rs=A7, e=A6, d=PORTB, n_lines=0, font=0):
    global mcp
    mcp = mcp23017.mcp32017()
    mcp.write_register(mcp23017.IODIRA, 0x00)
    mcp.write_register(mcp23017.OLATA, 0x01)
