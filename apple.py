import pygame, random

class Apple(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/apple.png').convert()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()

    def spawn(self):
        x_ = random.randint(31, 599)
        y_ = random.randint(29, 629)
        x = x_ - int(x_%30) + 15
        y = y_ - int(y_%30) + 15
        self.rect.center = (x, y)

    def is_apple_collected(self, x, y):
        if abs(self.rect.x-x) < 30 and abs(self.rect.y-y) < 30:
            return True
        else:
            return False

