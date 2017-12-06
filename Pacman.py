import pygame

class Pacman(pygame.sprite.Sprite):
    def __init__(self, x, y, img_file):
        #super().__init__()
        #super().__init__()
        pygame.init()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_file)
        self.screensize = (700,700)
        self.screen = pygame.display.set_mode(self.screensize)
        #self.size = self.image.Surface.get_size()
        self.x = x
        self.y = y
        self.direction = ''
        self.speed = 5
        self.isAlive = True
        self.isAtWall = False
        self.right_list = ['pacman_right_1.png','pacman_right_2.png']
        self.left_list = ['pacman_left_1.png','pacman_left_2.png']
        self.down_list = ['pacman_down_1.png','pacman_down_2.png']
        self.up_list = ['pacman_up_1.png','pacman_up_2.png']
        self.images = [self.right_list, self.left_list, self.down_list, self.up_list]
        for index in self.images:
                for i in index:
                        i = pygame.image.load(i).convert()
        
    def start(self):
        self.screen.blit(pygame.transform.smoothscale(self.image, (30,30)),(self.x,self.y))
    def move_left(self):
        self.x -= 1
                
    def move_right(self):
        self.x += 1
        
    def move_up(self):
        self.y -= 1
        
    def move_down(self):
        self.y += 1
    
    def get_position(self):
        return (self.x, self.y)

    def turn(self):
        if self.move_up():
                self.direction = "Up"
        elif self.move_down():
                self.direction = "Down"
        elif self.move_left():
                self.direction = "Left"
        elif self.move_right():
                self.direction = "Right"
        return self.direction
                
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
    def update(self):
        return ( self.get_direction())
        
        #array of images
        #cant push to remote if you have not updated
        #maybe make size of pacman smaller than rectangle
        #is the image array in pacman or controller?
        
        
