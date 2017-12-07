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
                
                self.mylist = []
        def createRect(self,surface):
                '''
                Creates a two-dimensional array
                input: Maze.txt
                output: 2-d list and 2-d array of rectangles
                '''
                self.file = open('Maze.txt','r')
                """
                for line in self.file:
                        #self.mylist.append([c for c in line])
                        for i in self.mylist:
                                for j in i:
                                        j = pygame.Rect(i*20,j*20,20,20)
                """
                        
                self.mylist = []
                for line in self.file:
                        self.mylist.append([c for c in line])
                        for i in range(0,len(self.mylist)):
                                for j in self.mylist[i]:
                                        coordinates = (i,j)
                                        self.drawRect(coordinates)

                self.file.close()
        def drawRect(self,coordinates):
                #self.mylist[i][j] = pygame.Rect(i*20,j*20,20,20)
                i = coordinates[0]
                j = coordinates[1]
                myrect = pygame.Rect(i*20,j*20,20,20)
                                
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
                for i in self.mylist:
                        pygame.draw.rect(screen, (255, 255, 255), i, 15)
        

