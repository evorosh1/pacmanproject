import sys
import pygame
import random
from Pacman import *
import Ghost
from os import path

class Controller:
	def __init__(self, width = 800, height = 600):
		pygame.init()
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width, self.height))
		self.pacman = Pacman.Pacman(100, 100, 'pacman_whole.png')
		self.ghosts = pygame.sprite.Group()
		self.background = pygame.Surface(self.screen.get_size()).convert()
	def mainLoop(self):
		pygame.key.set_repeat(1, 30)
		self.ghosts.add(Ghost.Ghost('red_left_2.png', 170, 80, 6))
		self.ghosts.add(Ghost.Ghost('blue_up_2.png', 190, 80, 6))
		self.ghosts.add(Ghost.Ghost('pink_down_2.png', 210, 80, 6))
		self.ghosts.add(Ghost.Ghost('orange_up_2.png', 230, 80, 6))	
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
			self.sprites.draw(self.screen)
			pygame.display.flip()

def main():
	main_window = Controller()
	main_window.mainLoop()
main()
