# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 02:05:59 2021

@author: sjoer
"""

import pygame
import serial
import time
from led import Led
import sys



def check_events(arduino, led1, led2, led3, led4):
    """Checks for Mousepresses and quit events. If quit event is detected
    the Serial connection is closed so that the port does not remain open.
    This would lead to the port not being accesible until cable is taken
    out and put back in again. Then the window is closed.
    
    If a Mouse Button down event is detected it checks whether the mouse
    was hovering over a LED image. If it was the led state will be changed
    
    Input:
        arduino: serial.Serial object
        led1: led.Led object
        led2: led.Led object
        led3: led.Led object
        led4: led.Led object
    
    return:
        does not return anything"""
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            arduino.close()
            sys.exit()
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get Coordinates of where mouse when it was clicked
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            # Check if any of leds have been clicked. Becomes True
            # when it has been clicked and becomes False when it has 
            # Not been clicked
            led1_clicked = led1.rect.collidepoint(mouse_x, mouse_y)
            led2_clicked = led2.rect.collidepoint(mouse_x, mouse_y)
            led3_clicked = led3.rect.collidepoint(mouse_x, mouse_y)
            led4_clicked = led4.rect.collidepoint(mouse_x, mouse_y)
                
            if led1_clicked:
                led_clicked(arduino, led1)
                
            elif led2_clicked:
                led_clicked(arduino, led2)
                    
            elif led3_clicked:
                led_clicked(arduino, led3)
                    
            elif led4_clicked:
                led_clicked(arduino, led4)
            
        

def arduino_write(arduino, x):
    """funtion that sends serial byte data to arduino. Waits 20 
    milliseconds between writing data to not overload the arduino.
    Input data is a string and is converted to bytes so it arduino can read it
    as serial data.
    
    Input:
        x: String to be converted to byte
    return values:
        No return Values
        
    """
    
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.03)

    
def led_clicked(arduino, led):
    """Updates the state of the led if it has been clicked from True to
    False or False to True. Then updates the message based on the state of
    The LED. Which Pin the LED is connected to and whether it is on or off
    (0 or 1) is send to the aruduino in the format (PIN:STATE).
    
    Input:
        arduino: serial.Serial object
        led: led.Led object
        
    Return:
        Does not return anything"""
    
    led.update_state()
    led.update_message()
    arduino_write(arduino, (str(led.pin) + ':' + str(int(led.state))))