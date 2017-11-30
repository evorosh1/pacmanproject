import pygame
import sys
import Ghost
import Pacman
class Maze:
    def __init__(self):
        pygame.init()
        mywall = {
            "%" = drawWall()
            "." = createPellet()
            "o" = createPowerPellet()
            "G" = insertGhost()
            "P" = insertPacman()}
    def drawWall(self):
        pygame.draw.line()
    def createPellet(self):
        pygame.draw.circle(self, white, (mylist[i]), 2, width=2)
    def createPowerPellet(self):
        pygame.draw.circle(self, blue, (mylist[i]), 4, width=4)
    def insertGhost(self):
        for i in range(4):
            self.ghost.append(ghost.Ghost("Boogie", x, y, 'ghost.png' ))
            self.sprites = pygame.sprite.Group(self.enemies)
    def insertPacman(self):
        
