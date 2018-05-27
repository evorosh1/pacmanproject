import pygame
#import Wall
import random
from Pacman import MovingSprite

class Ghost(MovingSprite):
  """
  Initializes a Ghost object
  Params: 
  Returns: none
  """
  def __init__(self, maze, x, y):
    self.images = [ maze.make_image('red_up_2.png') ]
    super( Ghost, self ).__init__( maze, x, y, 15 )

  def update( self ) :
    if self.next_pos is None :
      moves = [ self.move_up, self.move_down, self.move_left, self.move_right ]
      move  = random.choice( moves )
      while not move() :
        move  = random.choice( moves )
    super( Ghost, self ).update()