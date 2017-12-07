import pygame
import sys
import Ghost
import Pacman

class Maze():

#max/min x/y
#disable move_up/down etc
        def __init__(self,imgfile):

                '''
                Initializes Maze class
                inputs: N/A
                outputs: loaded image
                '''
                pygame.init()
                self.empty_maze = pygame.image.load(imgfile).convert()
                #self.pacman = pygame.image.load('pacman_whole.png').convert()
                self.mylist = []
        def createRect(self):
                '''
                Creates a two-dimensional array
                input: Maze.txt
                output: 2-d list and 2-d array of rectangles
                '''
                self.file = open('Maze.txt','r')
                for line in self.file:
                        self.mylist.append([c for c in line])
                        if c == "%":
                                for i in range(0,len(self.mylist)):
                                        for j in range(0,self.mylist[i]):
                                                self.mylist[i][j] = pygame.Rect(i*20,j*20,20,20)
                self.file.close()
                return self.mylist
        def showWalls(self):
                '''
                loads the maze image
                inputs: n/a
                outputs: maze image to the controller
                '''
                return image
        def if_collides(self, other):
                for i in self.mylist:
                        if self.mylist[i][j].colliderect(other):
                                print("no")
        def draw_rectangle(self, screen):
                for i in range(0,len(self.mylist)):
                                for j in range(0,self.mylist[i]):
                                        pygame.draw.rect(screen, 'white', self.mylist[i][j], width = 15)
        
