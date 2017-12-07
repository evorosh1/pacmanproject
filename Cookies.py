import pygame

class Cookies(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
	"""
	Creates Cookies object
	params: none
	returns: none
	"""
        pygame.sprite.Sprite.__init__(self)
        self.screensize = (700,700)
        self.screen = pygame.display.set_mode(self.screensize)
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
         
    def give_coord_cookies(self):
	"""
	Returns list of tuples of cookie coordinates
	params: none
	returns: self.cp
	"""
        self.cp = [(65, 670), (400,600), (600, 335), (165, 400), (370, 250), (470, 470)]
        return self.cp
    def give_coord_scookies(self):
	"""
	Returns coordinates of special cookies
	params: none
	returns: self.scp
	"""
        self.scp = [(40, 40), (650, 120), (315, 100), (620, 565)]
        return self.scp
        
    def draw_c(self):
	"""
	Draws cookie to the screen
	params: none
	returns: none
	"""
        for i in range(len(self.cp)):
            self.screen.blit(self.cookie,self.cp[i])
    def draw_sc(self):
        for i in range(len(self.scp)):
            self.screen.blit(self.specialcookie,self.scp[i])
