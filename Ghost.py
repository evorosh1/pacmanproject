import Controller
import pygame
#import Wall
import random

class Ghost(pygame.sprite.Sprite):
	"""
	Initializes a Ghost object
	Params: 
	Returns: none
	"""
	def __init__(self, img_file, name, x, y, color, speed):
		self.image = pygame.image.load(img_file).convert_alpha()
		self.rect = self.image.get_rect()
		self.name = name
		self.rect.x = x 
		self.rect.y = y
		#self.size = pygame.Surface.get_size()
		self.direction = ''
		self.color = color
		self.speed = speed
		self.isAtWall = False
	
	def turnRandom(self):
		self.direction = random.choice('left', 'right', 'up', 'down')
	
		if self.direction == 'left':
			self.rect.x -= self.speed
		if self.direction == 'right':
			self.rect.x += self.speed
		if self.direction == 'up':
			self.rect.y += self.speed
		if self.direction == 'down':
			self.rect.y -= self.speed
	
	def getPosition(self):	
		return (self.rect.x, self.rect.y)
	
	def changeState(self):
		pass
		
		