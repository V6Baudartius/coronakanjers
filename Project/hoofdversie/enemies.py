from gfx import *
import pygame, os, math, sys, time
print (__name__)

class monster():
    def __init__(self, x, y, speed):
        self.speed = speed
        self.x = x
        self.y = y
        self.sprite = imgload('monster.png')
    
    def update(self):
        draw(self.sprite, self.x, self.y)
        self.x += self.speed