import Controller
import Wall
import pygame
import turtle
import Controller
import Cookies

#  Wall?
# Github

class Pacman:
	def __init__(self, x, y, img_file):
		self.xcoord = x
		self.ycoord = y
		self.direction = ''
		self.hitGhost = False
		self.curPoints = 0
		self.isAlive = True
		self.isAtWall = False
	
	def turn(self, direction):
		#requires user input in wasd keys; first event will be a turn
		#how to keep the pacman moving continuously?
		#how to program in the wall so that the pacman is unable to move when it hits it
		#how to test code...
		if direction == w:
			self.direction = 'up'
			while isAtWall == False:
				self.ycoord += 1
		if direction == a:
			self.direction = 'right'
			while isAtWall == False:
				self.xcoord += 1
		if direction == s:
			self.direction = 'down'
			while isAtWall == False:
				self.ycoord -= 1
		if direction == d:
			self.direction = 'left'
			while isAtWall == False:
				self.ycoord -= 1
		return self.direction
	def.getPosition(self):
		return xcoord, ycoord

		
		