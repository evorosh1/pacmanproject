import pygame
import sys

class Maze:

#max/min x/y
#disable move_up/down etc
        def __init__(self, width, height ):
                '''
		Initializes Maze class
		inputs: N/A
		outputs: loaded image
		'''
                pygame.init()
                '''
                Creates a two-dimensional array
                input: Maze.txt
                output: 2-d list and 2-d array of rectangles
                '''
                self.maze = ['1111111111111111111111111111',
                             '1000000000000000000000000001',
                             '1001110111110110111110111101',
                             '1001110111110110111110111101',
                             '1000000000000110111110111101',
                             '1000000000000000000000000001',
                             '1011110110011111110110111101',
                             '1011110110011111110110111101',
                             '1000000110000110000110000001',
                             '1111100111100110011110011111',
                             '1111100111100110011110011111',
                             '1111100110000000000110011111',
                             '1111100110000000000110011111',
                             '1111100110011111100110011111',
                             '0000000000011111100000000000',
                             '0000000000011111100000000000',
                             '1111110110000000000110111111',
                             '1111110110000000000110111111',
                             '1111110110111111110110111111',
                             '1111110110111111110110111111',
                             '1000000000000110000000000001',
                             '1011110111110110111110111101',
                             '1011110111110110111110111101',
                             '1000110000000000000000110001',
                             '1100110000111111110000110011',
                             '1100110110111111110110110011',
                             '1000000110000110000110000001',
                             '1000000110000110000110000001',
                             '1011111111110110111111111101',
                             '1000000000000000000000000001',
                             '1111111111111111111111111111']
                self.rows = len( self.maze )
                self.cols = len( self.maze[0] )
                
                # self.size = ( width, height )
                self.cell_size = ( width // self.cols, height // self.rows )
                self.image_size = ( self.cell_size[ 0 ] - 4 , self.cell_size[ 1 ] - 4 )
                self.size = ( self.cell_size[0] * self.cols, self.cell_size[1] * self.rows )
                
        def wall_positions(self):
                walllist = []
                for y in range(self.rows):
                        for x in range(self.cols):
                                if self.is_wall( ( x, y ) ) :
                                        walllist.append( ( self.get_x( x ), self.get_y( y ) ) )
        
                return walllist
        
        def newImageRect( self ) :
                return pygame.Rect( 0, 0, self.image_size[ 0 ], self.image_size[ 1 ] )
        
        def get_x( self, x ) :
                return x * self.cell_size[ 0 ] + 2
                                                
        def get_y( self, y ) :
                return y * self.cell_size[ 1 ] + 2
        
        def is_wall( self, pos ) :
                if 0 < pos[0] < self.cols and 0 < pos[1] < self.rows :
                        return self.maze[ pos[ 1 ] ][ pos[ 0 ] ] == '1'
                else :
                        return True
        
        def if_collides(self, other):
                '''
                checks if anything collides with the maze
                inputs: other object
                outputs: collision detection
                '''
                for i in self.mylist:
                        if self.mylist[i][j].colliderect(other):
                                print('no')


        def make_image( self, image_name ) :
                image = pygame.image.load(image_name).convert_alpha()
                pygame.transform.smoothscale( image, self.image_size )
                return image