import pygame
import Controller


class Cookies:
	def __init__(self, img_file, x, y):
		self.image = pygame.image.load(img_file).convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
	
	def disappear(self):
		pass