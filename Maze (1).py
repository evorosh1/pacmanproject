import pygame
import sys
import Ghost
import Pacman
class Maze:

    def __init__(self):
        pygame.init()
        self.file = open('Maze.txt','r')
        for symbol in self.file:
            if symbol == "%":
                insertWall()
            elif symbol == ".":
                insertPellet()
            elif symbol == "o":
                insertCookie()
            elif symbol == "G":
                insertGhost()
            elif symbol == "P":
                insertPacman()
                
        self.empty_maze = pygame.image.load('empty_maze.png').convert()
	self.pacman = pygame.load('.png').convert()
	
    def showWall(self):
	return image, image.get_rect()
    def insertWall(self):
        pygame.draw.line()
    def insertPellet(self):
        pygame.draw.circle(self, white, (mylist[i]), 2, width=2)
    def insertCookie(self):
        pygame.draw.circle(self, blue, (mylist[i]), 4, width=4)
    def insertGhost(self):
        for i in range(4):
            self.ghost.append(ghost.Ghost("Boogie", x, y, 'ghost.png' ))
            self.sprites = pygame.sprite.Group(self.enemies)
    def insertPacman(self):
