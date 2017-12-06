import pygame
import Controller
import Pacman


class Cookies(pygame.sprite.Sprite):
	def __init__(self, img_file, x, y, type):
                pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(img_file).convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.type = ''
		self.size = pygame.Surface.get_size()
		self.pacman = Pacman
                self.specialcookie
        def get_postion(self):
                
	def disappear(self):
                eaten = False
                while not eaten:
                        if (self.pacman.get_position == self.cookie)
                        
	
	def getType(self):
		return self.type
	
