import pygame

class Pacman():
	def __init__(self, x, y, img_file):
		#super().__init__()
		#super().__init__()
		pygame.init()
		self.rect = []
		self.image = ['pacman_whole.png','pacman_right_1.png','pacman_right_2.png','pacman_left_1.png','pacman_left_2.png','pacman_up_1.png','pacman_up_2.png','pacman_down_1.png','pacman_down_2.png']
		for i in self.image:
			i = pygame.image.load(i).convert_alpha()
			self.rect.append(i.get_rect())
		#self.size = self.image.Surface.get_size()
		self.rect.x = 2
		self.rect.y = 2
		self.direction = ''
		self.speed = 5
		self.isAlive = True
		self.isAtWall = False
	
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
		print("Updating the position")
		
		#array of images
		#cant push to remote if you have not updated
		#maybe make size of pacman smaller than rectangle
		#is the image array in pacman or controller?