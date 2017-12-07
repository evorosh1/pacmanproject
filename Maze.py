import pygame
import sys
import Ghost
import Pacman
class Maze:

#max/min x/y
#disable move_up/down etc
	def __init__(self):

		'''
		Initializes Maze class
		inputs: N/A
		outputs: loaded image
		'''
		pygame.init()
		self.empty_maze = pygame.image.load(imgfile).convert()
		self.pacman = pygame.load('pacman_whole.png').convert()

	def createRect(self):
                '''
                Creates a two-dimensional array
                input: Maze.txt
                output: 2-d list and 2-d array of rectangles
                '''
		self.file = open('Maze.txt','r')
		mylist = []
		for line in self.file:
			mylist.append([c for c in line])
			#if c == "%":
			for i in range(0,len(mylist)):
				for j in range(0,mylist[i]):
					mylist[i][j] = pygame.rect(i*20,j*20,20,20)
		self.file.close()
		return mylist
	def showWalls(self):
                '''
                loads the maze image
                inputs: n/a
                outputs: maze image to the controller
                '''
		return image
	
def mainLoop():
	mazey = Maze()
	print(mazey.createRect)
mainLoop()

