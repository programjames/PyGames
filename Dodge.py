import pygame
import math
pygame.init()
## Need to make a bullet image, and then make it into an array and save it here (so it will not have to load an external file).
## Also need to make the image.
## Same with the character image (perhaps a differently colored bullet?)
bullet_img=pygame.Surface((1,1))
bullet_img.fill((0,0,255))
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
        self.points=[]
        self.img_width=self.img.get_width()
        self.img_height=self.img.get_height()
        for x in range(self.img_width):
            for y in range(self.img_height):
                if self.img.get_at((x,y))[3]!=0:
                    self.points.append([x,y])
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
        self.points=[]
        self.img_width=self.img.get_width()
        self.img_height=self.img.get_height()
        for x in range(self.img_width):
            for y in range(self.img_height):
                if self.img.get_at((x,y))[3]!=0:
                    self.points.append([x,y])
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
    def update_dir(self):
        x,y=pygame.mouse.get_pos()
        self.dir=math.atan2(y-pos[1],x-pos[0])
    def test_collide(self,b_list):
        for bullet in b_list:
            for point in bullet.points:
                for p in self.points:
                    if p[0]+self.pos[0]==point[0]+bullet.pos[0] and p[1]+self.pos[1]==point[1]+bullet.pos[1]:
                        return True
        return False
def make_bullet():
    global w,h
    pos=[int(math.random()*w),int(math.random()*h)]
    dir=int(random()*360)
    speed=0.1
    return Bullet(pos,dir,speed,bullet_img,w,h)
w,h=500,500
screen=pygame.display.set_mode((w,h))
bullet_list=[make_bullet() for i in range(10)]
player=Character(make_bullet())
while True:
    pygame.display.fill((255,255,255))
    for bullet in bullet_list:
        bullet.move()
        bullet.blit(screen)
    player.update_dir()
    player.move()
    player.blit(screen)
    pygame.display.update()
    if player.test_collide(b_list):
        break
