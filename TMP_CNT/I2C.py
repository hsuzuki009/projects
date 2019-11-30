#!/paty/to/python
# -*- coding: utf-8 -*-
import smbus
import time

class I2ctask:
        def __init__(self):
                print '[init]'
                self.bus = smbus.SMBus(1)

        def I2c_write(self,device,adr,value):
#                print '[write]'
                self.bus.write_byte_data(device, adr, value)
        def I2c_read(self,device,adr):
#                print '[read]'
                rd_data = self.bus.read_byte_data(device, adr)
                return rd_data

