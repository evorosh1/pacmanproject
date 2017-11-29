import Controller
import Wall
import pygame
import turtle
import Controller
import Cookies

#  Wall?
# Github

class Pacman(pygame.sprite.Sprite):
	def __init__(self, x, y, img_file):
		self.image = pygame.image.load(img_file).convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.speed = 5
		self.direction = ''
		self.isAlive = True
		self.isAtWall = False
	
	def turn(self, direction):
		#requires user input in wasd keys; first event will be a turn
		#how to keep the pacman moving continuously?
		#how to program in the wall so that the pacman is unable to move when it hits it
		#how to test code...
		if direction == "w":
			self.direction = 'up'
			self.rect.y += 1
		if direction == "a":
			self.direction = 'right'
			self.rect.x += 1
		if direction == "s":
			self.direction = 'down'
			self.rect.y -= 1
		if direction == "d":
			self.direction = 'left'
			self.rect.x -= 1
	def move(self):
		self.direction += self.speed
		
		
	def.getPosition(self):
		return xcoord, ycoord

		
		