import pygame
import random
from Cookies import StaticObject

class MovingSprite(StaticObject):
    def __init__(self, maze, x, y, speed ):
        self.speed  = speed
        self.next_pos = None
        self.distance = 0
        super( MovingSprite, self ).__init__(maze, x, y)
    
    def move_left(self):
        try_pos = ( self.cur_pos[0] - 1, self.cur_pos[1] )
        return self.try_move( try_pos )
            
    def move_right(self) :
        try_pos = ( self.cur_pos[0] + 1, self.cur_pos[1] )        
        return self.try_move( try_pos )
        
    def move_up(self):
        try_pos = ( self.cur_pos[0], self.cur_pos[1] - 1 )
        return self.try_move( try_pos )
        
    def move_down(self):
        try_pos = ( self.cur_pos[0], self.cur_pos[1] + 1 )
        return self.try_move( try_pos )
        
    def try_move( self, try_pos ) :
        if not self.next_pos and not self.maze.is_wall( try_pos ) :
            self.next_pos = try_pos
            self.distance = 0
            return True
        else :
            return False

    def update(self) :
        self.image = self.images[ ( self.distance // 10 ) % len( self.images) ]
        if self.next_pos :
            self.distance += 1
            if self.distance == self.speed :
                self.cur_pos = self.next_pos
                self.next_pos = None
                super( MovingSprite, self ).update()
            else :
                self.rect.x = int( self.maze.get_x( self.cur_pos[0] + ( self.next_pos[0] - self.cur_pos[0] ) * self.distance / self.speed ) )
                self.rect.y = int( self.maze.get_y( self.cur_pos[1] + ( self.next_pos[1] - self.cur_pos[1] ) * self.distance / self.speed ) )
        else :
            super( MovingSprite, self ).update()

class Pacman(MovingSprite):
    def __init__(self, maze, x, y ):
        self.right_list = [ maze.make_image( 'pacman_right_1.png' ), maze.make_image( 'pacman_right_2.png' ) ]
        self.left_list = [maze.make_image( 'pacman_left_1.png'),maze.make_image( 'pacman_left_2.png') ]
        self.down_list = [maze.make_image( 'pacman_down_1.png'),maze.make_image( 'pacman_down_2.png')]
        self.up_list   = [maze.make_image( 'pacman_up_1.png'),maze.make_image( 'pacman_up_2.png') ]
        self.images    = self.right_list
        
        super( Pacman, self ).__init__( maze, x, y, 20 )
        self.start_pos = ( x, y )

    def move_left(self):
        if super( Pacman, self ).move_left() :
            self.images = self.left_list

    def move_right(self) :
        if super( Pacman, self ).move_right() :
            self.images = self.right_list
        
    def move_up(self):
        if super( Pacman, self ).move_up() :
            self.images = self.up_list
            
    def move_down(self):
        if super( Pacman, self ).move_down() :
            self.images = self.down_list