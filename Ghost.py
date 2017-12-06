import pygame
#import Wall
import random

class Ghost(pygame.sprite.Sprite):
	"""
	Initializes a Ghost object
	Params: 
	Returns: none
	"""
	def __init__(self, img_file, x, y, speed):
		super().__init__()
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(img_file).convert_alpha()
		self.rect = self.image.get_rect()
		self.x = self.rect.x
		self.y = self.rect.y
		#self.size = pygame.Surface.get_size()
		self.direction = ''
		self.speed = speed
		self.state = 'chase'
		self.isAtWall = False
		self.red_down = ['red_down_1.png', 'red_down_2.png']
		self.red_right = ['red_right_1.png', 'red_right_2.png']
		self.red_left = ['red_left_1.png', 'red_left_2.png']
		self.red_up = ['red_up_1.png', 'red_up_2.png']
		
		self.blue_down = ['blue_down_1.png', 'blue_down_2.png']
		self.blue_right = ['blue_right_1.png', 'blue_right_2.png']
		self.blue_left = ['blue_left_1.png', 'blue_left_2.png']
		self.blue_up = ['blue_up_1.png', 'blue_up_2.png']
		
		self.pink_down = ['pink_down_1.png', 'pink_down_2.png']
		self.pink_right = ['pink_right_1.png', 'pink_right_2.png']
		self.pink_left = ['pink_left_1.png', 'pink_left_2.png']
		self.pink_up = ['pink_up_1.png', 'pink_up_2.png']
		
		self.orange_up = ['orange_up_1.png', 'orange_up_2.png']
		self.orange_down = ['orange_down_1.png', 'orange_down_2.png']
		self.orange_right = ['orange_right_1.png', 'orange_right_2.png']
		self.orange_left = ['orange_left_1.png', 'orange_left_2.png']
		
		self.ghost_images = [self.red_down, self.red_up, self.red_left, self.red_right, self.blue_down, self.blue_up, self.blue_left, self.blue_right, self.pink_up, self.pink_down, self.pink_right, self.pink_left, self.orange_up, self.orange_down, self.orange_left, self.orange_right]
		for i in range(len(self.ghost_images)):
			for j in range(len(self.ghost_images[i])):
				self.ghost_images[i][j] = pygame.image.load(self.ghost_images[i][j])
	def turn(self):
		if direction == up:
			self.direction = "Up"
			self.ycoord += 1
		if direction == right:
			self.direction = "Right"
			self.xcoord += 1
		if direction == down:
			self.direction = "Down"
			self.ycoord -= 1
		if direction == left:
			self.direction = "Left"
			self.ycoord -= 1

	def move_left(self):
		self.x -= 1
	def move_right(self):
		self.x += 1
	def move_up(self):
		self.y += 1
	def move_down(self):
		self.y -= 1
	
	def getPosition(self):	
		return (self.rect.x, self.rect.y)
		
	def get_direction(self):
		self.dir = self.turn()
		if self.dir == "Down":
				if self.x % 2 == 0:
					  self.img = self.down_list[0]
				else:
					  self.img = self.down_list[1]
		elif self.dir == "Up":
				if self.x % 2 == 0:
					  self.img = self.up_list[0]
				else:
					  self.img = self.up_list[1]
		elif self.dir == "Left":
				if self.x % 2 == 0:
					  self.img = self.left_list[0]
				else:
					  self.img = self.left_list[1]
		elif self.dir == "Right":
				if self.x % 2 == 0:
					  self.img = self.right_list[0]
		else:
				self.img = self.right_list[1]
		
		self.loaded_img = pygame.image.load(self.img)
		self.resized_img = pygame.transform.smoothscale(self.loaded_img, (30,30))
		return self.resized_img
	
	def changeState(self):
		if self.state == 'chase':
			pass
		if self.state == 'scatter':
			pass
		if self.state == 'frightened':
			pass
	def edible(self):
		pass
	def getState(self):
		return self.state
		
	def update(self):
		print("updating position")
