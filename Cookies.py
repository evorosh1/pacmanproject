import pygame
import Pacman
import Maze


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
	def draw_postions(self):
		self.specialcookie = [(10, 10), (10, 650), (300, 200), (400, 500)]
		self.cookie = [(45, 660), (75, 140), (60, 320), (189, 575), (370, 250), (470, 470)]
		self.allcoords = []
		self.allcoords.add(self.cookie)
		self.allcoords.add(self.specialcookie)
		for i in range(len(self.specialcookie)):
                        pygame.draw.circle(Surface,(63,63,63), i, 3)    
												
	def disappear(self):
		eat = False
		self.score = 0
		while not eaten:
                        if len(self.allcoords) == 0
                                return self.score
                        else:
                                eaten = pygame.sprite.spritecollide(self.pacman, self.allcoords, True, collided)												 
                                for eat in eaten:
                                        self.score += 1
                                        pygame.draw.circle(Surface,(0,0,0), eat, 3)
                                return self.score
	def getType(self):
		return self.type
	
