import pygame

class Pacman(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        #super().__init__()
        #super().__init__()
        pygame.init()
        pygame.sprite.Sprite.__init__(self)
        self.screensize = (580,620)
        self.screen = pygame.display.set_mode(self.screensize)
        #self.size = self.image.Surface.get_size()
        self.image = pygame.image.load(image).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = ''
        self.speed = 5
        '''
        self.isAlive = True
        self.isAtWall = False
        self.right_list = ['pacman_right_1.png','pacman_right_2.png']
        self.left_list = ['pacman_left_1.png','pacman_left_2.png']
        self.down_list = ['pacman_down_1.png','pacman_down_2.png']
        self.up_list = ['pacman_up_1.png','pacman_up_2.png']
        self.images = [self.right_list, self.left_list, self.down_list, self.up_list]
        for index in self.images:
                for i in index:
                        i = pygame.image.load(i)
        '''
    def start(self):
        self.screen.blit(pygame.transform.smoothscale(self.image, (30,30)),(self.rect.x,self.rect.y))
    def move_left(self):
        self.rect.x -= 3
        
        
    def move_right(self):
        self.rect.x += 3
        
        
    def move_up(self):
        self.rect.y -= 3
        
    def move_down(self):
        self.rect.y += 3
    
    def get_position(self):
        return (self.rect.x, self.rect.y)
    
    
    '''
    def turn(self):
        if self.move_up() == True:
                if self.x % 2 == 0:
                      self.img = self.up_list[0]
                else:
                      self.img = self.up_list[1]
        elif self.move_down():
                if self.x % 2 == 0:
                      self.img = self.down_list[0]
                else:
                      self.img = self.down_list[1]
        elif self.move_left():
                if self.x % 2 == 0:
                      self.img = self.left_list[0]
                else:
                      self.img = self.left_list[1]
        elif self.move_right():
                self.direction = "Right"
                if self.x % 2 == 0:
                      self.img = self.right_list[0]
        else:
                self.img = self.right_list[1]
        return self.img
    
    def get_img(self):
        self.img = self.turn()
        self.loaded_img = pygame.image.load(self.img).convert()
        self.rect = self.loaded_img.get_rect()
        self.resized_img = self.rect.inflate_ip(30,30)
        return self.resized_img
     '''
    def get_img(self):
        self.img = 'pacman_left_1.png'
        self.image = pygame.image.load(self.img).convert_alpha()
        self.resized_img = pygame.transform.smoothscale(self.image, (30,30))
        return self.resized_img
    
    def update(self):
        return (self.rect.x, self.rect.y)
        
        
        #array of images
        #cant push to remote if you have not updated
        #maybe make size of pacman smaller than rectangle
        #is the image array in pacman or controller?
        
        
