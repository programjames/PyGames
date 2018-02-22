import pygame
import math
pygame.init()
## Need to make a bullet image, and then make it into an array and save it here (so it will not have to load an external file).
## Also need to make the image.
## Same with the character image (perhaps a differently colored bullet?)
bullet_img=None
character_img=None
class Bullet():
    def __init__(self,pos,dir,speed,img,width,height):
        self.pos=pos
        self.pos[0]=self.pos[0]%width
        self.pos[1]=self.pos[1]%h
        self.pos2=pos
        self.pos2[0]=self.pos[0]+width
        self.pos2[1]=self.pos[1]+height
        self.dir=dir
        self.speed=speed
        self.img=img
        self.dx=math.sin(dir*math.pi/180)
        self.dy=math.cos(dir*math.pi/180)
        self.w=width
        self.h=height
    def move(self):
        self.pos[0]+=self.dx*self.speed
        self.pos[1]+=self.dy*self.speed
        self.pos[0]=self.pos[0]%self.w
        self.pos[1]=self.pos[1]%self.h
        self.pos2[0]=self.pos[0]+self.w
        self.pos2[1]=self.pos[1]+self.h
    def blit(self,screen):
        screen.blit(self.img,self.pos)
        screen.blit(self.img,self.pos2)
class Character():
    def __init__(self,pos,dir,speed,img,width,height):
        self.pos=pos
        self.pos[0]=self.pos[0]%width
        self.pos[1]=self.pos[1]%h
        self.pos2=pos
        self.pos2[0]=self.pos[0]+width
        self.pos2[1]=self.pos[1]+height
        self.dir=dir
        self.speed=speed
        self.img=img
        self.dx=math.sin(dir*math.pi/180)
        self.dy=math.cos(dir*math.pi/180)
        self.w=width
        self.h=height
    def move(self):
        self.pos[0]+=self.dx*self.speed
        self.pos[1]+=self.dy*self.speed
        self.pos[0]=self.pos[0]%self.w
        self.pos[1]=self.pos[1]%self.h
        self.pos2[0]=self.pos[0]+self.w
        self.pos2[1]=self.pos[1]+self.h
    def blit(self,screen):
        screen.blit(self.img,self.pos)
        screen.blit(self.img,self.pos2)
    def change_dir(self,new_dir):
        self.dir=new_dir
def make_bullet():
    global w,h
    pos=[int(math.random()*w),int(math.random()*h)]
    dir=int(random()*360)
    speed=0.1
    return Bullet(pos,dir,speed,bullet_img,w,h)
w,h=500,500
screen=pygame.display.set_mode((w,h))
bullet_list=[make_bullet() for i in range(10)]
