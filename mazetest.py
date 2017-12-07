import Maze
import pygame

def main():
    screen = pygame.display.set_mode((580,620))
    maze = Maze.Maze()
    maze.createRect(screen)
    
    #pygame.draw.rect(screen, (255,255,255), rect, width = 5)
    


main()
