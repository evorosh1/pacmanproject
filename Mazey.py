import pygame
import sys

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
                self.surface = surface
                
                for line in self.file:
                        #self.mylist.append([c for c in line])
                        for i in range(0,len(self.mylist)):
                                for j in self.mylist[i]:
                                        self.mylist[i][j] = pygame.Rect(20*i,20*j,20,20)
                                        pygame.draw.rect(screen, (255,255,255), self.mylist[i][j], width = 10)
                                        print(self.mylist)
                
               
                self.file.close()            
                
                

        def if_collides(self, other):
                '''
                checks if anything collides with the maze
                inputs: other object
                outputs: collision detection
                '''
                for i in self.mylist:
                        if self.mylist[i][j].colliderect(other):
                                print('no')

