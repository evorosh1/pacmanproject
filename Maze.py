import pygame
import sys
import Ghost
import Pacman
class Maze:

#max/min x/y
#disable move_up/down etc
        def __init__(self):
                pygame.init()      

        def createRect(self):
                self.file = open('Maze.txt','r')
                mylist = []
                for line in self.file:
                        mylist.append([c for c in line])
                        if c == "%":
                                for i in range(0,len(mylist)):
                                        for j in range(0,mylist[i]):
                                                mylist[i][j] = pygame.rect(i*20,j*20,20,20)
                self.file.close()
                return mylist
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
 
