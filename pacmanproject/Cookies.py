import pygame

class StaticObject(pygame.sprite.Sprite):
    def __init__(self, maze, x,y ):
        super( StaticObject, self).__init__()
        self.maze = maze
        self.rect = self.maze.newImageRect()
        self.cur_pos = (x, y)
        self.update()

    def update( self ) :
        self.rect.x = self.maze.get_x( self.cur_pos[0] )
        self.rect.y = self.maze.get_y( self.cur_pos[1] )
        

class OrangeCookies( StaticObject ) :
    def __init__(self, maze, x,y ):
        super( OrangeCookies, self).__init__(maze, x, y )
        self.image = self.maze.make_image( 'orange_down_1.png' )

class PinkCookies( StaticObject ) :
    def __init__(self, maze, x,y ):
        super( PinkCookies, self).__init__(maze, x, y )
        self.image = self.maze.make_image( 'pink_down_1.png' )