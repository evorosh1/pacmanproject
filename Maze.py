import pygame
import sys
import Ghost
import Pacman
class Maze:

#max/min x/y
#disable move_up/down etc
	def __init__(self):
		pygame.init()
		self.file = open('Maze.txt','r')
		mylist = []
		for line in self.file:
			mylist.append([c for c in line])
			#if c == "%":
                                #Pacman.canMove = False
		for i in range(0,len(mylist)):
			for j in range(0,mylist[i]):
				mylist[i][j] = pygame.Rect(37 * i, 37 * j, 37, 37)
								
		self.empty_maze = pygame.image.load(imgfile).convert()
		self.pacman = pygame.image.load('pacman_whole.png').convert()
		self.file.close()
		return mylist
	#def canMove(self):
	#        if (self.x > 663):
	#                move_right.enabled = False
	#        elif (self.x < 37):
	#               move_left.enabled = False
	#        elif (self.y > 663):
	#                move_up.enabled = False
	#        elif (self.y < 37):
	#                move_down.enabled = False
	def showWalls(self):
		return image
	def makeWalls(self):
		pass
	def insertGhost(self):
		for i in range(4):
			self.ghost.append(ghost.Ghost("Boogie", x, y, 'ghost.png' ))
			self.sprites = pygame.sprite.Group(self.enemies)
	def insertPacman(self):
		pass
		
