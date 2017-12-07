import sys
import pygame
import random
import Pacman
import Ghost
import Maze
import Cookies
#import textbox
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
        self.sgroup.add(Cookies.Cookies(332, 462,'orange_down_1.png'))
        self.sgroup.add(Cookies.Cookies(54, 531,'orange_down_1.png'))
        self.sgroup.add(Cookies.Cookies(307, 350,'orange_down_1.png'))
        self.sgroup.add(Cookies.Cookies(125, 354,'orange_down_1.png'))
        self.sgroup.add(Cookies.Cookies(370, 240,'orange_down_1.png'))
        self.sgroup.add(Cookies.Cookies(470, 410,'orange_down_1.png'))
        self.scgroup = pygame.sprite.Group()
        self.scgroup.add(Cookies.Cookies(539, 106,'pink_down_1.png'))
        self.scgroup.add(Cookies.Cookies(33, 35,'pink_down_1.png'))
        self.scgroup.add(Cookies.Cookies(261, 89,'pink_down_1.png'))
        self.scgroup.add(Cookies.Cookies(510, 500,'pink_down_1.png'))
        self.ghosts = pygame.sprite.Group()
        self.ghosts.add(Ghost.Ghost('blue_up_2.png', 539, 106))
        self.ghosts.add(Ghost.Ghost('blue_up_2.png', 33, 35))
        self.ghosts.add(Ghost.Ghost('blue_up_2.png', 261, 89))
        self.ghosts.add(Ghost.Ghost('blue_up_2.png', 510, 500))
        #self.ghost=(Ghost.Ghost('pink_up_2.png', 300, 300))
        self.cookiescollected=0
        self.lives = 3

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
            for self.ghost in self.ghosts:
                self.ghost.start()
            self.ghosts.draw(self.screen)
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
            self.ghosts.draw(self.screen)
            self.pacman.update()
            self.pacman.get_position()
            for self.ghost in self.ghosts:
                self.screen.blit(self.ghost.get_img(), (self.ghost.get_direction()))
            for self.ghost in self.ghosts:
                self.ghost.update()
            #pygame.sprite.spritecollide(self.pacman, self.walls) collide function if walls would work
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
                    self.text = self.font.render("You died", True, (255,255,255),True)
                    self.screen.blit(self.text,(2,250))
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
            if(self.lives == 0):
                self.cook = str(self.cookiescollected)
                self.font = pygame.font.SysFont('Arial', 60)
                self.text = self.font.render("You Lose, you got"+self.cook , True, (255,255,255),True)
                self.screen.blit(self.text,(2,250))
                pygame.time.delay(1000)
                running = False
                sys.exit()

def main():
        main_window = Controller()
        main_window.message_to_screen(("Use arrow keys to move pacman, press q to end game, if the ghost eats you 3 times you die, eat all the pellets to win"), (255,255,255), 15, (5,600))
        main_window.game_intro("Press Spacebar to start playing Pacman :)")
        main_window.mainLoop()
main()
