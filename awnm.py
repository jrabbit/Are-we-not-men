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
                elif event.type == KEYDOWN:
                    if ((event.key == K_RIGHT)
                    or (event.key == K_LEFT)
                    or (event.key == K_UP)
                    or (event.key == K_DOWN)):
                        self.water.move(event.key)
            """Check for collision"""
            lstCols = pygame.sprite.spritecollide(self.water, self.sand_sprites, True)
            """Update the amount of pellets eaten"""
            self.water.volume = self.water.volume + len(lstCols)
            self.sand_sprites.draw(self.screen)
            self.water_sprites.draw(self.screen)
            pygame.display.flip()
    def LoadSprites(self):
        """Load the sprites that we need"""
        self.water = Water()
        self.water_sprites = pygame.sprite.RenderPlain((self.water))  
        """figure out how many pellets we can display"""
        nNumHorizontal = int(self.width/64)
        nNumVertical = int(self.height/64)       
        """Create the Pellet group"""
        self.sand_sprites = pygame.sprite.Group()
        """Create all of the pellets and add them to the 
        pellet_sprites group"""
        for x in range(nNumHorizontal):
            for y in range(nNumVertical):
                self.sand_sprites.add(Sand(pygame.Rect(x*64, y*64, 64, 64)))

class Water(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.image, self.rect = load_image('water.png',-1)
        self.volume = 0
        self.x_dist = 15
        self.y_dist = 15
        #ME GO TOO FAR!
    def move(self, key):
        """Move your self in one of the 4 directions according to key"""
        """Key is the pyGame define for either up,down,left, or right key
        we will adjust ourselves in that direction"""
        xMove = 0;
        yMove = 0;

        if (key == K_RIGHT):
            xMove = self.x_dist
        elif (key == K_LEFT):
            xMove = -self.x_dist
        elif (key == K_UP):
            yMove = -self.y_dist
        elif (key == K_DOWN):
            yMove = self.y_dist
        self.rect.move_ip(xMove,yMove);

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