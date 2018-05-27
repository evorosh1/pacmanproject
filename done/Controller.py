import sys
import pygame
import random
import Pacman
import Ghost
import Maze
import Cookies
import Walls
#import textbox
from os import path

class Controller(object):
    def __init__(self, width = 580, height = 700):
        '''
        initializes the controller class and sets up the window
        inputs: width and height of window
        outputs: pacman screen
        '''
        pygame.init()
        self.maze = Maze.Maze( width, height )
        
        self.width = width
        self.height = height
        
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.pacman = Pacman.Pacman( self.maze, 21, 21 )
        self.pgroup = pygame.sprite.GroupSingle(self.pacman)
        self.maze_image = pygame.image.load('empty_maze.png')
        self.resized = pygame.transform.smoothscale(self.maze_image, self.maze.size)
        
        self.mgroup = pygame.sprite.Group()
        wall_image  = self.maze.make_image('blue_down_1.png')
        for coord in self.maze.wall_positions():
            self.mgroup.add(Walls.Walls(coord[0], coord[1], wall_image))
        #self.maze_image
        #self.pacman_rect = ?????????????
        self.sgroup = pygame.sprite.Group()
        self.taken_pos   = set( [ ( self.pacman.start_pos ) ] )

        self.sgroup  = pygame.sprite.Group()
        self.scgroup = pygame.sprite.Group()
        self.ghosts = pygame.sprite.Group()
        
        self.add_sprite( 6, Cookies.OrangeCookies, self.sgroup )
        self.add_sprite( 4, Cookies.PinkCookies, self.scgroup )
        self.add_sprite( 4, Ghost.Ghost, self.ghosts )
        Ghost
        #self.ghosts.add(Ghost.Ghost('red_up_2.png', 539, 106))
        #self.ghosts.add(Ghost.Ghost('red_up_2.png', 33, 35))
        #self.ghosts.add(Ghost.Ghost('red_up_2.png', 261, 89))
        #self.ghosts.add(Ghost.Ghost('red_up_2.png', 510, 500))
        #self.ghost=(Ghost.Ghost('pink_up_2.png', 300, 300))
        self.cookiescollected=0
        self.lives = 3

        
    def add_sprite( self, num_sprites, sprite_class, group ) :
        for cookie in range(num_sprites) :
            try_pos = ( random.randint( 0, self.maze.cell_size[ 0 ] ), random.randint( 0, self.maze.cell_size[ 1 ] ) )
            while self.maze.is_wall( try_pos ) or try_pos in self.taken_pos :
                try_pos = ( random.randint( 0, self.maze.cell_size[ 0 ] ), random.randint( 0, self.maze.cell_size[ 1 ] ) )
            self.taken_pos.add( try_pos )
            group.add(sprite_class( self.maze, try_pos[0], try_pos[1] ) )

    def message_to_screen(self, msg, color, size, coords):
        '''
        displays message on screen
        inputs: message, color, size, and coordinates (tuple)
        outputs: message on screen
        '''
        self.font = pygame.font.SysFont('Arial', size)
        self.text = self.font.render(msg, True, color)
        self.screen.blit(self.text,coords)
    def game_intro(self, msg):
        '''
        displays an intro message on the screen
        inputs: message
        outputs: message relaying directions
        '''
        intro = True
        while intro:
            pygame.draw.rect(self.screen, (255,255,255), [0,240,580,100])
            self.message_to_screen(msg,(0,0,0), 35,(5, 250))
            for event in pygame.event.get():
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_SPACE):
                        self.screen.fill((0,0,0),(0,0,580,620))
                        self.message_to_screen(("Use arrow keys to move pacman, press q to end game, if the ghost eats you 3 times you die, eat all the pellets to win"), (255,255,255), 15, (5,705))
                        self.screen.blit(self.resized, (0,0))
                        intro = False
            pygame.display.flip()
            
    
    def mainLoop(self):
        '''
        runs events for the game
        inputs: key presses
        outputs: events, updating pacman
        '''
        pygame.key.set_repeat(1, 40)
        running = True
        while running:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                        running = False
                        sys.exit()
                elif (event.type == pygame.KEYDOWN):
                        if (event.key == pygame.K_q):
                                running = False
                                pygame.quit()
                                quit()
                        elif(event.key == pygame.K_UP):
                                self.pacman.move_up()
                        elif(event.key == pygame.K_DOWN):
                                self.pacman.move_down()
                        elif(event.key == pygame.K_LEFT):
                                self.pacman.move_left()
                        elif(event.key == pygame.K_RIGHT):
                                self.pacman.move_right()
                
                #self.ghost.move()
                #if event.type == pygame.KEYUP:
                #checks if pacman gets eaten by ghost or if ghost eats pacman
            #if(pygame.sprite.spritecollideany(self.pacman, self.ghosts) == True):
                #if(self.ghosts.edible == True):
                    #self.ghosts.kill()
                    #del self.ghost
                #else:
                    #self.pacman.lives -= 1
                #break
            
            self.screen.fill((0,0,0),(0,0, self.maze.size[0], self.maze.size[1]))
            self.screen.blit(self.resized, (0, 0))
            self.sgroup.draw(self.screen)
            self.scgroup.draw(self.screen)
            self.ghosts.draw(self.screen)
            self.pacman.update()
            for self.ghost in self.ghosts:
                self.ghost.update()
                    
            self.ate = pygame.sprite.spritecollide(self.pacman, self.sgroup, True)
            if self.ate:
                self.cookiescollected += 1
            self.ate2= pygame.sprite.spritecollide(self.pacman, self.scgroup, True)
            if self.ate2:
                self.cookiescollected += 1
            
            self.coll = pygame.sprite.spritecollide(self.pacman, self.ghosts,False)
            if self.coll:
                #pygame.time.Clock.tick
                while self.coll:
                    pygame.time.delay(1000)
                    self.font = pygame.font.SysFont('Arial', 60)
                    self.text = self.font.render("lost life", True, (255,255,255),True)
                    self.screen.blit(self.text,(2,250))
                    #self.pacman.start_again()  
                    self.lives -= 1
                    self.coll = False
               # if pygame.time.Clock.get_time <= 7000:
                #    self.font = pygame.font.SysFont('Arial', 60)
                 #   self.text = self.font.render("You Win", True, (255,255,255),True)
                  #  self.screen.blit(self.text,(2,250))
                   # pygame.time.delay(1000)
                    #running = False
                    #sys.exit()
                    
            self.sgroup.update()
            self.scgroup.update()
            self.ghosts.draw(self.screen)
            self.pgroup.draw(self.screen)
            #self.screen.blit(self.pacman.get_img(), (self.pacman.rect.x, self.pacman.rect.y))
            self.mgroup.draw(self.screen)
            pygame.display.flip()
            """
            redraw background
            call upate on sprites
            redraw sprites
            call flip
            """
            if(self.lives == 0):
                self.cook = str(self.cookiescollected)
                self.font = pygame.font.SysFont('Arial', 60)
                self.screen.fill((0,0,0),(0,0, 580, 620))
                self.text = self.font.render("You Lose, you got"+self.cook , True, (255,255,255),True)
                self.screen.blit(self.text,(2,250))
                pygame.time.delay(1000)
                running = False
                sys.exit()
                '''
            if len(self.sgroup) == 0:
                if len(self.scgroup) == 0:
                    self.screen.fill((0,0,0),(0,0,580,620))
                    self.font = pygame.font.SysFont('Arial', 80)
                    self.text = self.font.render("YOU WON", True, (255,255,255),True)
                    self.screen.blit(self.text,(200,250))
                    running = False
                    '''
        #if running == False:
         #   self.screen.fill((0,0,0),(0,0,580,620))
          #  self.font = pygame.font.SysFont('Arial', 80)
           # self.text = self.font.render("YOU WON", True, (255,255,255),True)
                    

if __name__ == "__main__" :
        main_window = Controller()
        #main_window.message_to_screen(("Use arrow keys to move pacman, press q to end game, if the ghost eats you 3 times you die, eat all the pellets to win"), (255,255,255), 15, (5,600))
        #main_window.game_intro("Press Spacebar to start playing Pacman :)")
        main_window.mainLoop()

