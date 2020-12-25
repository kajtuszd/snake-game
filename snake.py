import pygame

(s_width, s_height) = (30,30)

GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
AZURE = (51, 255, 255)

class Snake(pygame.sprite.Sprite):

    rect = []
    image = []
    tail_img = pygame.Surface((s_width, s_height))
    tail_img.fill(BLUE)

    green_img = pygame.Surface((s_width, s_height))
    green_img.fill(AZURE)

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.length = 1
        self.score = 0
        self.rect.append(pygame.Rect(self.green_img.get_rect()))
        self.rect[0].x = 300
        self.rect[0].y = 330

    def increase(self):
        self.score += 1
        self.length += 1
        self.rect.append(pygame.Rect(self.tail_img.get_rect()))

    def draw(self, surface):
        if self.length > 0:
            for i in range(1, self.length):
                surface.blit(self.tail_img,(self.rect[i].x, self.rect[i].y))
        surface.blit(self.green_img,(self.rect[0].x, self.rect[0].y))


    def move(self, direction):
        self.rect[0].x += direction[0]
        self.rect[0].y += direction[1]

        for i in range(self.length-1, 0, -1):
            self.rect[i].x = self.rect[i-1].x
            self.rect[i].y = self.rect[i-1].y

        if self.length > 1:
            self.rect[1].x = self.rect[0].x - direction[0]
            self.rect[1].y = self.rect[0].y - direction[1]


    def is_outside_frame(self):
        if (self.rect[0].x >= 600):
            return True
        if (self.rect[0].y > 600):
            return True
        if (self.rect[0].x < 0):
            return True
        if (self.rect[0].y <= 0):
            return True
        return False

    '''
    checks collision between head and body
    '''
    def is_collision(self):
        x_ = self.rect[0].x
        y_ = self.rect[0].y
        if self.length < 4:
            return False
        return self.is_field_busy(3, x_, y_) # check if current head position is busy

    def is_field_busy(self, node, x, y):
        for field in range(node, self.length):
            if abs(self.rect[field].x - x) < 30 and abs(self.rect[field].y - y) < 30:
                return True
        return False




