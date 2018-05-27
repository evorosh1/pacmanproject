import pygame
import sys
import Maze

class Please:
    def __init__(self):
        pygame.init()
        self.size = (580,620)
        self.screen = pygame.display.set_mode(self.size)
        self.test = Maze.Maze()
        self.list1 = self.test.lets_draw()
    def draww(self):
        pygame.key.set_repeat(1, 40)
        for self.tup in self.list1:
            self.x = self.tup[0]
            self.y = self.tup[1]
            pygame.draw.rect(self.screen, (255,255,255), (self.x, self.y, 20,20))
            pygame.display.flip()
                #self.screen.fill((255,255,255),(self.x, self.y, 20,20))
        pygame.display.update()
def main():
    main_window = Please()
    main_window.draww()
main()
