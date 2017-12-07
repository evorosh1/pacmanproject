import pygame
#import Wall
import random

class Ghost(pygame.sprite.Sprite):
  """
  Initializes a Ghost object
  Params: 
  Returns: none
  """
  def __init__(self, image, x, y):
    self.screensize = (580,620)
    self.screen = pygame.display.set_mode(self.screensize)
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load(image).convert()
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    #self.size = pygame.Surface.get_size()
    self.direction = ''
    self.state = 'chase'
    self.isAtWall = False
    
    '''
    self.red_down = ['red_down_1.png', 'red_down_2.png']
    self.red_right = ['red_right_1.png', 'red_right_2.png']
    self.red_left = ['red_left_1.png', 'red_left_2.png']
    self.red_up = ['red_up_1.png', 'red_up_2.png']
    
    self.blue_down = ['blue_down_1.png', 'blue_down_2.png']
    self.blue_right = ['blue_right_1.png', 'blue_right_2.png']
    self.blue_left = ['blue_left_1.png', 'blue_left_2.png']
    self.blue_up = ['blue_up_1.png', 'blue_up_2.png']
    
    self.pink_down = ['pink_down_1.png', 'pink_down_2.png']
    self.pink_right = ['pink_right_1.png', 'pink_right_2.png']
    self.pink_left = ['pink_left_1.png', 'pink_left_2.png']
    self.pink_up = ['pink_up_1.png', 'pink_up_2.png']
    
    self.orange_up = ['orange_up_1.png', 'orange_up_2.png']
    self.orange_down = ['orange_down_1.png', 'orange_down_2.png']
    self.orange_right = ['orange_right_1.png', 'orange_right_2.png']
    self.orange_left = ['orange_left_1.png', 'orange_left_2.png']
    def turn(self):
    if direction == up:
      self.direction = "Up"
      self.ycoord += 1
    if direction == right:
      self.direction = "Right"
      self.xcoord += 1
    if direction == down:
      self.direction = "Down"
      self.ycoord -= 1
    if direction == left:
      self.direction = "Left"
      self.ycoord -= 1
       def turn(self):
        def move_left(self):
    self.rect.x -= 1
  def move_right(self):
    self.rect.x += 1
  def move_up(self):
    self.rect.y -= 1
  def move_down(self):
    self.rect.y += 1

    '''
    self.listdir= ["Up","Down", "Left", "Right"]


  def get_direction(self):

        self.index = random.randint(0,3)
        self.dir = self.listdir[self.index]
        if self.dir  == "Down":
          self.rect.y += 2               
        
        elif self.dir == "Up":
          self.rect.y -= 2
                
        elif self.dir == "Left":
          self.rect.x -= 2
        elif self.dir == "Right":
          self.rect.x += 2
        return (self.rect.x, self.rect.y)
  def start(self):  
    self.screen.blit(pygame.transform.smoothscale(self.image, (30,30)),(self.rect.x, self.rect.y))
  def get_img(self):
    self.img = 'red_up_2.png'
    self.image = pygame.image.load(self.img).convert_alpha()
    self.resized_img = pygame.transform.smoothscale(self.image, (30,30))
    return self.resized_img
                
  def changeState(self):
    if self.state == 'chase':
      pass
    if self.state == 'scatter':
      pass
    if self.state == 'frightened':
      pass
  def edible(self):
    pass
  def getState(self):
    return self.state
    
  def update(self):
    return( self.rect.x, self.rect.y)

