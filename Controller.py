import sys
import pygame
import random
import Pacman
import Ghost
import Maze
import Cookies
from os import path

class Controller:
    def __init__(self, width = 580, height = 700):
        '''
        initializes the controller class and sets up the window
        inputs: width and height of window
        outputs: pacman screen
        '''
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.pacman = Pacman.Pacman(337, 520, 'pacman_whole.png')
        self.maze_image = pygame.image.load('empty_maze.png')
        self.resized = pygame.transform.smoothscale(self.maze_image, (580,620))
        #self.maze_image
        #self.pacman_rect = ?????????????
        self.sgroup = pygame.sprite.Group()
        self.sgroup.add(Cookies.Cookies(65, 670,'orange_down_1.png'))
        self.sgroup.add(Cookies.Cookies(400,600,'orange_down_1.png'))
        self.sgroup.add(Cookies.Cookies(600, 335,'orange_down_1.png'))
        self.sgroup.add(Cookies.Cookies(165, 400,'orange_down_1.png'))
        self.sgroup.add(Cookies.Cookies(370, 250,'orange_down_1.png'))
        self.sgroup.add(Cookies.Cookies(470, 470,'orange_down_1.png'))
        self.scgroup = pygame.sprite.Group()
        self.scgroup.add(Cookies.Cookies(650, 120,'pink_down_1.png'))
        self.scgroup.add(Cookies.Cookies(40, 40,'pink_down_1.png'))
        self.scgroup.add(Cookies.Cookies(315, 100,'pink_down_1.png'))
        self.scgroup.add(Cookies.Cookies(620, 565,'pink_down_1.png'))
        self.ghosts = pygame.sprite.Group()
        self.ghosts.add(Ghost.Ghost('red_left_2.png', 170, 80))
        self.ghosts.add(Ghost.Ghost('blue_up_2.png', 190, 80))
        self.ghosts.add(Ghost.Ghost('pink_down_2.png', 210, 80))
        self.ghosts.add(Ghost.Ghost('orange_up_2.png', 230, 80))
        self.ghost=(Ghost.Ghost('pink_up_2.png', 300, 300)) 
        self.pacman.lives = len(self.ghosts)

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
            self.ghost.start()
            self.sgroup.draw(self.screen)
            self.scgroup.draw(self.screen)
            self.screen.blit(self.resized, (580,620))
            self.pacman.start()
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
            
            self.screen.fill((0,0,0),(0,0, 580, 620))
            self.screen.blit(self.resized, (0, 0))
            self.sgroup.draw(self.screen)
            self.scgroup.draw(self.screen)
            self.pacman.update()
            self.pacman.get_position()
            self.screen.blit(self.ghost.get_img(), (self.ghost.get_direction()))
            pygame.sprite.spritecollide(self.pacman, self.sgroup, True)                                                 
            pygame.sprite.spritecollide(self.pacman, self.scgroup, True)    
            self.sgroup.update()
            self.scgroup.update()
            #self.ghosts.update()
            self.screen.blit(self.pacman.get_img(), (self.pacman.rect.x, self.pacman.rect.y))
            #self.sprites.draw(self.screen)
            pygame.display.flip()
            #redraw the entire screen
            """
            redraw background
            call upate on sprites
            redraw sprites
            call flip
            """
            #if(self.pacman.lives == 0):
                #print("You lose")

def main():
        main_window = Controller()
        main_window.message_to_screen(("Use arrow keys to move pacman, press q to end game, if the ghost eats you 3 times you die, eat all the pellets to win"), (255,255,255), 15, (5,620))
        main_window.game_intro("Press Spacebar to start playing Pacman :)")
        main_window.mainLoop()
main()
