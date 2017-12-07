import pygame

class Cookies(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        pygame.sprite.Sprite.__init__(self)
        self.screensize = (580,620)
        self.screen = pygame.display.set_mode(self.screensize)
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
         
    def give_coord_cookies(self):
        self.cp = [(54, 555), (332, 497), (498, 335), (137, 332), (307, 250), (390, 470)]
        return self.cp
    def give_coord_scookies(self):
        self.scp = [(33, 33), (539, 99.5), (261, 83), (515, 468)]
        return self.scp
        
    def draw_c(self):
        for i in range(len(self.cp)):
            self.screen.blit(self.cookie,self.cp[i])
    def draw_sc(self):
        for i in range(len(self.scp)):
            self.screen.blit(self.specialcookie,self.scp[i])

