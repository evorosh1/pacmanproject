import pygame

class Pacman(pygame.sprite.Sprite):
	def __init__(self, img_file):
		#super().__init__()
		#super().__init__()
		pygame.init()
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(img_file).convert()
		self.rect = self.image.get_rect()
		self.x = self.rect.x
		self.y = self.rect.y
		#self.size = self.image.Surface.get_size()
		self.direction = ''
		self.speed = 5
		self.isAlive = True
		self.isAtWall = False
		self.index = 0
		self.images = []
		self.right_list = ['pacman_right_1.png','pacman_right_2.png']
		self.left_list = ['pacman_left_1.png','pacman_left_2.png']
		self.down_list = ['pacman_down_1.png','pacman_down_2.png']
		self.up_list = ['pacman_up_1.png','pacman_up_2.png']
		for i in self.images:
			i = pygame.image.load(i)
		
	
	def turn(self):
		if self.direction == 'up':
			self.rect.y += 1
		if direction == right:
			self.direction = 'right'
			self.rect.x += 1
		if direction == down:
			self.direction = 'down'
			self.rect.y -= 1
		if direction == left:
			self.direction = 'left'
			self.rect.y -= 1

	def move_left(self):
		self.direction = "left"
		self.images = self.left_list
	def move_right(self):
		self.x += 1
		self.images = self.right_list
	def move_up(self):
		self.y += 1
		self.images = self.up_list
	def move_down(self):
		self.y -= 1
		self.images = self.down_list
	
	def get_position(self):
		return (self.rect.x, self.rect.y)
		
	def	update(self):
		self.turn()
		"""
		if self.index < (len(self.images) - 1):
			self.index += 1
		else:
			self.index = 0
		return self.images[self.index]
		"""
		
		
	def getDirection(self):
		return self.direction
		
		#array of images
		#cant push to remote if you have not updated
		#maybe make size of pacman smaller than rectangle
		#is the image array in pacman or controller?
