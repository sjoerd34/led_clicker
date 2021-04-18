# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 22:31:50 2021

@author: sjoer
"""
import pygame
import sys
from led import Led
from message import Message
import serial
import time
import led_functions as lf

# Location of Led images
rood = 'afbeeldingen/rood_ledje_klein2.png'
blauw = 'afbeeldingen/blauw_ledje_klein2.png'
groen = 'afbeeldingen/groen_ledje_klein2.png'
geel = 'afbeeldingen/geel_ledje_klein2.png'

# Start Serial communication on port arduino is connected to.
# Send timeout error when it takes longer than 0.1 seconds to connect to
# Arduino on port 5
arduino = serial.Serial(port='COM3', baudrate=115200, timeout=0.1)




def run_led():
    """run the Arduino Led control file"""
    # Initialize pygame
    pygame.init()
    
    # Create the pygame window with certain dimensions
    screen = pygame.display.set_mode((1200, 800))
    
    # Name displayed in Tab
    pygame.display.set_caption("Arduino Led control")
    
    # Create led instances
    red_led = Led(1, rood, screen, 10)
    yellow_led = Led(2, geel, screen, 12)
    green_led = Led(3, groen, screen, 4)
    blue_led = Led(4, blauw, screen, 5)
    
    
    while True:
        
        # Update the state of the screen
        pygame.display.flip()
        
        # Give the screen a background with specified color
        screen.fill((255, 255, 255))
        
        # Draw The led instances on the screen
        red_led.blitme()
        blue_led.blitme()
        green_led.blitme()
        yellow_led.blitme()
        
        #check if led has been pressed and respond accordingly
        lf.check_events(arduino, red_led, yellow_led,
                        green_led, blue_led)
                
                
                    
run_led()
