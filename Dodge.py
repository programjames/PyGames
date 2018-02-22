import pygame
import math
pygame.init()
## Need to make a bullet image, and then make it into an array and save it here (so it will not have to load an external file).
## Also need to make the image.
## Same with the character image (perhaps a differently colored bullet?)
class Bullet():
    def __init__(self,pos,dir,speed,img,w,h):
        self.pos=pos
        self.pos[0]=self.pos[0]%w
        self.pos[1]=self.pos[1]%h
        self.pos2=pos
        self.pos2[0]=self.pos[0]+w
        self.pos2[1]=self.pos[1]+h
        self.dir=dir
        self.speed=speed
        self.img=img
        self.dx=math.sin(dir*math.pi/180)
        self.dy=math.cos(dir*math.pi/180)
    def move(self):
        self.pos[0]+=self.dx*self.speed
        self.pos[1]+=self.dy*self.speed
        self.pos[0]=self.pos[0]%w
        self.pos[1]=self.pos[1]%h
        self.pos2[0]=self.pos[0]+w
        self.pos2[1]=self.pos[1]+h
    def blit(self,screen):
        screen.blit(self.img,self.pos)
        screen.blit(self.img,self.pos2)
w,h=500,500
screen=pygame.display.set_mode((w,h))
