#!/usr/bin/python

import os
import sys
import time
import usb.core
import serial


class launchControl:
   def __init__(self):
      self.dev = usb.core.find(idVendor=0x2123, idProduct=0x1010)
      self.ser = serial.Serial("/dev/ttyUSB0", 115200)

      if self.dev is None:
         raise ValueError('Launcher not found.')
      if self.dev.is_kernel_driver_active(0) is True:
         self.dev.detach_kernel_driver(0)
      self.dev.set_configuration()

   def up(self):
      self.dev.ctrl_transfer(0x21,0x09,0,0,[0x02,0x02,0x00,0x00,0x00,0x00,0x00,0x00]) 

   def down(self):
      self.dev.ctrl_transfer(0x21,0x09,0,0,[0x02,0x01,0x00,0x00,0x00,0x00,0x00,0x00])

   def left(self):
      self.dev.ctrl_transfer(0x21,0x09,0,0,[0x02,0x04,0x00,0x00,0x00,0x00,0x00,0x00])

   def right(self):
      self.dev.ctrl_transfer(0x21,0x09,0,0,[0x02,0x08,0x00,0x00,0x00,0x00,0x00,0x00])

   def stop(self):
      self.dev.ctrl_transfer(0x21,0x09,0,0,[0x02,0x20,0x00,0x00,0x00,0x00,0x00,0x00])

   def fire(self):
      self.dev.ctrl_transfer(0x21,0x09,0,0,[0x02,0x10,0x00,0x00,0x00,0x00,0x00,0x00])

   def lightOn(self):
       self.ser.write(b"255,255,255\n")
   
   def lightOff(self):
       self.ser.write(b"0,0,0\n")

sentry = launchControl()
