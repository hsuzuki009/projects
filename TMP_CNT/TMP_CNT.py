#!/paty/to/python
# -*- coding: utf-8 -*-
import smbus
import time

i2c = smbus.SMBus(1)
device = 0x05
adr0 = 0x13
adr1 = 0x01
  

while True:
#    block = i2c.read_i2c_block_data(device, adr0, 1)
#    x = block[0]
#    print"%d" %x
#    time.sleep(0.1)
    i2c.write_byte_data(device, adr1, 0xf4)
    time.sleep(0.1)
    i2c.write_byte_data(device, adr1, 0xf8)
    time.sleep(0.1)
    


