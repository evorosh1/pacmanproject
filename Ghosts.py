import Controller
import Pacman
import pygame
import Wall

class Ghosts:
	"""
	Initializes a Ghost object
	Params:
	Returns: 
	
	"""
	def __init__(self, x, y):
		self.xcoord = x #for ghosts and pacman, where do we decide their placement since it is not the user's job?
						#In other words where do we initialize the game? 
		self.ycoord = y
	
	def move(self, random = FALSE):
		Pacman.getPosition()
		
		
	
	
	
	
	"""	
	getwd
	git init
	git add
	git add .
	git remote add origin https://github.com/wafflethief/CS-110-Final-Project--Pacman.git
	git remote -v
	git push origin master
	git add Pacman.py
	ls
	pwd
	cd Documents/CS110_Project/
	ls
	exit #to leave
	"""