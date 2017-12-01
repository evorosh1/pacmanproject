import sys
import pygame
import random
import Pacman
import Ghost

class Controller:
    def __init__(self, width = 800, height = 600):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        
    def mainLoop(self):
        pygame.key.set_repeat(1,50)
		
		self.Ghosts.add(Ghost.Ghost(img_file, name, c, y, orange, 6))
        while True:
            self.background.fill((250, 250, 250))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_UP):
                        self.pacman.move_up()
                    elif(event.key == pygame.K_DOWN):
                        self.pacman.move_down()
                    elif(event.key == pygame.K_LEFT):
                        self.pacman.move_left()
                    elif(event.key == pygame.K_RIGHT):
                        self.pacman.move_right()
            #checks if pacman gets eaten by ghost
            for i in range(len(self.ghost)):
                if(pygame.sprite.collide_rect(self.pacman, self.ghost[i])):
                    if(self.ghost[i].edible == True):
                        self.ghost[i].kill()
                        del self.ghost[i]
                    else:
                        self.pacman.lives -= 1
                    break
			
            if(self.pacman.lives == 0):
                self.pacman.kill()
            #redraw the entire screen
            self.screen.blit(self.background, (0, 0))
            self.sprites.draw(self.screen)
            pygame.display.flip()


def main():
    main_window = Controller()
    main_window.mainLoop()
main()
