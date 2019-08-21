import smbus

channel = 1

address = 0x60

bus = smbus.SMBus(channel)

bus.write_byte_data(address, 0x01, 0xFF)
bus.write_byte_data(address, 0x05, 0xAA)
bus.write_byte_data(address, 0x06, 0x02)