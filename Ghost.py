import pygame
#import Wall
import random

class Ghost(pygame.sprite.Sprite):
	"""
	self.red_ghost = ['red_left_1.png', 'red_left_2.png', 'red_right_1.png', 'red_right_2.png', 'red_up_1.png', 'red_up_2.png', 'red_down_1.png', 'red_down_2.png']
	for i in self.red_ghost:
			i = pygame.image.load(i)
			self.red = self.image.get_rect()
		self.blue_ghost = ['blue_left_1.png', 'blue_left_2.png', 'blue_right_1.png', 'blue_right_2.png', 'blue_up_1.png', 'blue_up_2.png', 'blue_down_1.png', 'blue_down_2.png']
		for i in self.blue_ghost:
			i = pygame.image.load(i)
			
	"""
	"""
	Initializes a Ghost object
	Params: 
	Returns: none
	"""
	def __init__(self, img_file, x, y, speed):
		super().__init__()
		self.image = pygame.image.load(img_file).convert_alpha()
		self.rect = self.image.get_rect()
		self.x = self.rect.x
		self.y = self.rect.y
		#self.size = pygame.Surface.get_size()
		self.direction = ''
		self.speed = speed
		self.state = 'chase'
		self.isAtWall = False

	def turn(self):
		if direction == up:
			self.direction = 'up'
			self.ycoord += 1
		if direction == right:
			self.direction = 'right'
			self.xcoord += 1
		if direction == down:
			self.direction = 'down'
			self.ycoord -= 1
		if direction == left:
			self.direction = 'left'
			self.ycoord -= 1

	def move_left(self):
		self.x -= 1
	def move_right(self):
		self.x += 1
	def move_up(self):
		self.y += 1
	def move_down(self):
		self.y -= 1
	
	def getPosition(self):	
		return (self.rect.x, self.rect.y)
	
	def changeState(self):
		if self.state == 'chase':
			pass
		if self.state == 'scatter':
			pass
		if self.state == 'frightened':
			pass
	
	def getState(self):
		return self.state
		
	def update(self):
		print("updating position")