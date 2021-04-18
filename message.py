# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 04:11:48 2021

@author: sjoer
"""

import pygame

class Message():
    
    def __init__(self, width, height, centerx, centery, screen, msg):
        """Initialize method for Message function"""
        self.width = width
        self.height = height
        self.screen = screen
        self.msg = msg
        self.font = pygame.font.SysFont(None, 24)
        
         
        self.position_msg(centerx, centery, width, height)
        
        self.display_color = (255, 255, 255)
        self.text_color = (0,0,0)
        
        self.prep_msg(msg)
        
    def position_msg(self, cx, cy, width, height):
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.centerx = int(cx)
        self.rect.centery = int(cy)
   
    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, 
            self.display_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.centerx = self.rect.centerx
        self.msg_image_rect.centery = self.rect.centery
       
    def draw_display(self):
        self.screen.fill(self.display_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
       
        