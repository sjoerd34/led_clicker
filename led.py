# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 03:01:39 2021

@author: sjoer
"""

import pygame
from message import Message


class Led():
    
    def __init__(self, position, image, screen, pin, state = False):
        
        self.position = position
        self.image = pygame.image.load(image)
        self.state = state
        self.screen = screen
        self.pin = pin
        self.update_message()
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        
        
        # position of LED
        
        self.rect.centerx = int((self.screen_rect.right / 4)) * (self.position-0.5) 
        self.rect.centery = 0.25*self.screen_rect.bottom

        # state display
        self.state_display = Message(self.rect.width, 20,
                               self.rect.centerx, (self.rect.bottom + 20), 
                               self.screen, self.msg)
        
    
    def update_message(self):
        if self.state == True:
            self.msg = "ON"
        else:
            self.msg = "OFF"
    
    def update_state(self):
        self.state = not(self.state)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        self.state_display.prep_msg(self.msg)
        self.state_display.draw_display()