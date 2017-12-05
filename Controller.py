import sys
import pygame
import random
import Pacman
import Ghost
from os import path

class Controller:
	def __init__(self, width = 800, height = 600):
		pygame.init()
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width, self.height))
		self.background = pygame.Surface(self.screen.get_size()).convert_alpha()
		self.maze = pygame.image.load('0.png')
		self.maze_rect = self.maze.get_rect()
		self.pacman = Pacman.Pacman('pacman_whole.png')
		self.ghosts = pygame.sprite.Group()
		self.images = ['pacman_whole.png','pacman_right_1.png','pacman_right_2.png','pacman_left_1.png','pacman_left_2.png','pacman_up_1.png','pacman_up_2.png','pacman_down_1.png','pacman_down_2.png']
		for i in self.images:
			i = pygame.image.load(i)
		#self.rect = self.image.get_rect()
	def mainLoop(self):
		pygame.key.set_repeat(1, 30)
		
		self.ghosts.add(Ghost.Ghost('red_left_2.png', 170, 80, 6))
		self.ghosts.add(Ghost.Ghost('blue_up_2.png', 190, 80, 6))
		self.ghosts.add(Ghost.Ghost('pink_down_2.png', 210, 80, 6))
		self.ghosts.add(Ghost.Ghost('orange_up_2.png', 230, 80, 6))	
		
		while True:
			#self.screen.blit(self.background, (0, 0))
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
						self.pacman_rect.x += 1
						#pygame.Rect.move(self.pacman_rect(self.pacman_rect.x,self.pacman_rect.y))
						#for i in self.images:
							#self.screen.blit(self.images[i], self.pacman_rect.x, self.pacman_rect.y))
			#checks if pacman gets eaten by ghost
			#collisions = pygame.sprite.spritecollide(self
			#collidable = pygame.sprite.collide_mask
			#self.maze_rect.inflate(100,100)
			
			pygame.Rect.inflate(self.maze_rect,(1000, 1000))#(self.screen.get_width(), self.screen.get_height()))
			self.screen.blit(self.maze, (0,0))
			
			#if pygame.sprite.spritecollideany(self.pacman, self.ghosts):
			
			#redraw the entire screen
			#self.sprites.draw(self.screen)
			#pygame.display.flip()
			
def main():
	main_window = Controller()
	main_window.mainLoop()
main()
