import pygame

WIDTH = 1200

HEIGHT = 600

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sprite/Run__000.png')
        self.rect = pygame.Rect(100,100,100,100)
    
    def update(self, *args):
        #self.image = pygame.transform.scale(self.image,[100,100])
        pass

pygame.init()
game_window = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption('Infinite Runner')

playerGroup = pygame.sprite.Group()
player = Player()
playerGroup.add(player)

gameloop = True

def draw():
    game_window.fill([255,255,0])


while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
    pygame.display.update()