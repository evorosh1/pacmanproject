import Controller
import pygame
import Wall
import random

class Ghost:
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
		self.color = color
		self.speed = speed
		self.isAtWall = False
	
	def move_left(self):
		self.rect.x -= self.speed
	
	def move_right(self):
		self.rect.x += self.speed
	
	def move_up(self):
		self.rect.y += self.speed
	
	def move_down(self):
		self.rect.y -= self.speed
	
	def move(self, random = FALSE):
		Pacman.getPosition()
	
	def getPosition(self, self.rect):	
		self.rect.x
	
	def changeState(self):
		pass
		