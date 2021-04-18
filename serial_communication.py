# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 23:00:29 2021

@author: sjoer
"""

import serial
import time

arduino = serial.Serial(port='COM5', baudrate=9600, timeout=.1)

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data


while True:
    num = input("Enter a number: ")
    if num == 'q':
        arduino.close()
        print("Serieële communicatie beëidigt4")
        break
    else:
        value = write_read(num)
        print(value)