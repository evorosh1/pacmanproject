import sys
import pygame
import random
import Pacman
import Ghost
#import textbox
from os import path

class Controller:
    def __init__(self, width = 700, height = 750):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.pacman = Pacman.Pacman('pacman_whole.png')

        self.ghosts = pygame.sprite.Group()
        self.ghosts.add(Ghost.Ghost('red_left_2.png', 170, 80, 6))
        self.ghosts.add(Ghost.Ghost('blue_up_2.png', 190, 80, 6))
        self.ghosts.add(Ghost.Ghost('pink_down_2.png', 210, 80, 6))
        self.ghosts.add(Ghost.Ghost('orange_up_2.png', 230, 80, 6))     
        Pacman.lives = len(self.ghosts)
    def message_to_screen(self,msg, color, size, coords):
        pygame.init()
        self.font = pygame.font.SysFont('Arial', size)
        self.text = self.font.render(msg, True, color)
        self.screen.blit(self.text,coords)
    def game_intro(self, msg):
        intro = True
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.K_SPACE:
                    intro = False
            pygame.draw.rect(self.screen, (255,255,255), [0,300,700, 100])
            self.message_to_screen(msg,(0,0,0), 45,(5, 310))
            pygame.display.update()
    def mainLoop(self):
        pygame.key.set_repeat(1, 30)
        running = True
        while running:
            self.background.fill((250, 250, 250))
            pygame.Rect.inflate(self.maze_rect,(self.screen.get_width(), self.screen.get_height()))
            self.screen.blit(self.maze, self.maze_rect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                        if event.type == pygame.K_q:
                                pygame.quit()
                                quit()
                        if(event.key == pygame.K_UP):
                                self.pacman.move_up()
                        elif(event.key == pygame.K_DOWN):
                                self.pacman.move_down()
                        elif(event.key == pygame.K_LEFT):
                                self.pacman.move_left()
                        elif(event.key == pygame.K_RIGHT):
                                self.pacman.move_right()
                #elif(event.key == pygame.K_SPACE):
                #self.text.disappear()
                    #self.ghost.move()
                    #if event.type == pygame.KEYUP:
                #checks if pacman gets eaten by ghost
                #collisions = pygame.sprite.spritecollide(self
                #collidable = pygame.sprite.collide_mask
            for i in range(len(self.ghosts)):
                if(pygame.sprite.spritecollideany(self.pacman, self.ghosts) == True):
                    if(self.ghosts.edible == True):
                        self.ghosts.kill()
                        del self.ghost
                    else:
                        self.pacman.lives -= 1
                    break
            
            if(self.pacman.lives == 0):
                self.pacman.kill()
                #redraw the entire screen
                self.screen.blit(self.background, (0, 0))
                self.pacman.update()
                self.ghosts.update()
                self.screen.blit(self.pacman,self.pacman_re)
                self.sprites.draw(self.screen)
                pygame.display.flip()
                """
                redraw background
                call upate on sprites
                redraw sprites
                call flip
                """

def main():
        main_window = Controller()
        main_window.message_to_screen(("Use arrow keys to move pacman, press q to end game, if the ghost eats you 3 times you die, eat all the pellets to win"), (255,255,255), 15, (5,705))
        main_window.game_intro("Press Spacebar to start playing Pacman :)")
        main_window.mainLoop()
main()
