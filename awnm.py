#!/usr/bin/env python
# Are we not men?
# 2010. Jrabbit. GPL v3 or later.
#Support only offered for Lolcat linux
import time
import os, sys
import pygame
from pygame.locals import *
from helpers import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'
#boilerplate pygame used lovingly from http://www.learningpython.com/2006/03/12/creating-a-game-in-python-using-pygame-part-one/
class AWNMMain:
    """The Main AWNM Class - This class handles the main initialization and creating of the Game.""" 
    def __init__(self, width=640,height=480):
        """Initialize"""
        """Initialize PyGame"""
        pygame.init()
        """Set the window Size"""
        self.width = width
        self.height = height
        """Create the Screen"""
        self.screen = pygame.display.set_mode((self.width, self.height))
        
    def MainLoop(self):
        """This is the Main Loop of the Game"""
        """Load All of our Sprites"""
        self.LoadSprites();
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
            self.water_sprites.draw(self.screen)
            pygame.display.flip()
    def LoadSprites(self):
        """Load the sprites that we need"""
        self.water = Water()
        self.water_sprites = pygame.sprite.RenderPlain((self.water))  

class Water(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.image, self.rect = load_image('water.png',-1)
        self.volume = 0

class Sand(pygame.sprite.Sprite):
    def __init__(self, rect=None):
        pygame.sprite.Sprite.__init__(self) 
        self.image, self.rect = load_image('sand.png',-1)
        if rect != None:
            self.rect = rect

start = time.time()
print "Gee Brain, What do you want to do today?"
print "Same thing we do every day, Pinky -- try to take over the world!"

if __name__ == "__main__":
    MainWindow = AWNMMain()
    MainWindow.MainLoop()

print "we just wasted " + str(elapsed) + " seconds"