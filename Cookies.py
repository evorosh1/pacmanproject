import pygame
import Controller


class Cookies:
	def __init__(self, img_file):
		self.image = pygame.image.load(img_file).convert_alpha()
		self.rect = self.image.get_rect()
	
	def disappear(self):
		pass