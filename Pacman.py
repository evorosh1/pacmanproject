import pygame

class Pacman():
	def __init__(self, img_file):
		#super().__init__()
		#super().__init__()
		pygame.init()
		self.image = pygame.image.load(img_file).convert()
		self.rect = self.image.get_rect()
		#self.size = self.image.Surface.get_size()
		self.direction = ''
		self.speed = 5
		self.isAlive = True
		self.isAtWall = False
		self.index = 0
		self.images = ['pacman_whole.png','pacman_right_1.png','pacman_right_2.png','pacman_left_1.png','pacman_left_2.png','pacman_up_1.png','pacman_up_2.png','pacman_down_1.png','pacman_down_2.png']
		for i in self.images:
			i = pygame.image.load(i)
	def turn(self):
		if direction == up:
			self.direction = 'up'
			self.ycoord += 1
		if direction == right:
			self.direction = 'right'
			self.xcoord += 1
		if direction == down:
			self.direction = 'down'
			self.ycoord -= 1
		if direction == left:
			self.direction = 'left'
			self.ycoord -= 1

	def move_left(self):
		self.rect.x -= self.speed
	def move_right(self):
		self.rect.x += self.speed
	def move_up(self):
		self.rect.y += self.speed
	def move_down(self):
		self.rect.y -= self.speed
		
	#def.getPosition(self):
		#return (self.rect.x, self.rect.y)
	
	def update(self):
		self.index += 1
		if self.index >= len(self.images):
			self.index = 0
		
	def getDirection(self):
		return self.direction
		
		#array of images
		#cant push to remote if you have not updated
		#maybe make size of pacman smaller than rectangle
		#is the image array in pacman or controller?