import serial


print("Press CTRL+C to exit")
S = serial.Serial(port="/dev/ttyS0",baudrate="4800")
if not S.isOpen:
	S.open()

try:
	while True:
		S.write((input("> ") + '\n').encode("utf-8"))
except:
	print("exitting")
	S.close()
