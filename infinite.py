import pygame

WIDTH = 1200

HEIGHT = 600

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_run = [pygame.image.load('Desktop\Dev\Git\infiniterunner\sprites/Run__000.png'),
        pygame.image.load('Desktop\Dev\Git\infiniterunner\sprites/Run__001.png'),
        pygame.image.load('Desktop\Dev\Git\infiniterunner\sprites/Run__002.png'),
        pygame.image.load('Desktop\Dev\Git\infiniterunner\sprites/Run__003.png'),
        pygame.image.load('Desktop\Dev\Git\infiniterunner\sprites/Run__004.png'),
        pygame.image.load('Desktop\Dev\Git\infiniterunner\sprites/Run__005.png'),
        pygame.image.load('Desktop\Dev\Git\infiniterunner\sprites/Run__006.png'),
        pygame.image.load('Desktop\Dev\Git\infiniterunner\sprites/Run__007.png'),
        pygame.image.load('Desktop\Dev\Git\infiniterunner\sprites/Run__008.png'),
        pygame.image.load('Desktop\Dev\Git\infiniterunner\sprites/Run__009.png')
        ]
        self.image = pygame.image.load('Desktop\Dev\Git\infiniterunner\sprites/Run__000.png')
        self.rect = pygame.Rect(100,100,100,100)
        self.current_image = 0
    def update(self, *args):
        def move_player(self):
            self.current_image = (self.current_image + 1 ) % 10    
            self.image = self.image_run[self.current_image]
            self.image = pygame.transform.scale(self.image,[100,100])

pygame.init()
game_window = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption('Infinite Runner')

playerGroup = pygame.sprite.Group()
player = Player()
playerGroup.add(player)

gameloop = True

def draw():
    playerGroup.draw(game_window)

def update():
    playerGroup.update()


while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
    update()
    draw()
    pygame.display.update()