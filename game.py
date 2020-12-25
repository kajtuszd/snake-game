import pygame, os
from leaderboard import Leaderboard

GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
(f_width, f_height) = (600, 600)
(w_width, w_height) = (300, 100)

class Game(pygame.sprite.Sprite):

    def __init__(self):
        self.board = Leaderboard()
        pygame.sprite.Sprite.__init__(self)

    def draw_frame(self, screen):
        pygame.draw.rect(screen, (0,250,0), (0, 30, 600, 600), 5)

    def draw_white_rect(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (0, 0, 600, 30))

    def wait(self):
        flag = True
        while flag:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return True
                    if event.key == pygame.K_p:
                        flag = False
                        return False

    def render_leaderboard(self, screen):
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont('dejavuserif', 30, True, True)
        flag = True
        while flag:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                        flag = False

                    if event.key == pygame.K_r:
                        screen.fill((0, 0, 0))
                        self.board.reset()

            self.board.file = open("leaderboard.txt", "r")
            i = 110
            text = font.render("Leaderboard: ", False, (GREEN), (0, 0, 0))
            screen.blit(text, (50, 50))
            text1 = font.render("R - reset results ", False, (GREEN), (0, 0, 0))
            screen.blit(text1, (50, 450))
            for line in self.board.file:
                text = font.render(line[0: len(line)-1], False, (GREEN), (0, 0, 0))
                screen.blit(text, (50, i))
                i += 50
            pygame.display.flip()

        self.board.file.close()
        screen.fill((0, 0, 0))


    def render_welcome_view(self, screen, snake):
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont('dejavuserif', 30, True, True)
        flag = True
        while flag:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        flag = False
                        return True

                    elif event.key == pygame.K_s:
                        self.render_settings_view(screen, snake)

                    elif event.key == pygame.K_l:
                        self.render_leaderboard(screen)

                    elif event.key == pygame.K_ESCAPE:
                        flag = False
                        return False

            text0 = font.render('Move with arrows', False, (GREEN), (0, 0, 0))
            text1 = font.render('ESC - Exit', False, (GREEN), (0, 0, 0))
            text2 = font.render('P - Pause', False, (GREEN), (0, 0, 0))
            text3 = font.render('S - Go to settings', False, (GREEN), (0, 0, 0))
            text4 = font.render('L - Check leaderboard', False, (GREEN), (0, 0, 0))
            text5 = font.render('Press ENTER to start game', False, (GREEN), (0, 0, 0))
            screen.blit(text0, (50, 120))
            screen.blit(text1, (50, 170))
            screen.blit(text2, (50, 220))
            screen.blit(text3, (50, 300))
            screen.blit(text4, (50, 350))
            screen.blit(text5, (50, 430))
            pygame.display.flip()

    def render_exit_view(self, screen, score):
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont('dejavuserif', 30, True, True)
        flag = True
        while flag:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()


                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        flag = False
                    if event.key == pygame.K_RETURN:
                        return True

            text1 = font.render('Your score: {0}'.format(str(score)), False, (GREEN), (0, 0, 0))
            text2 = font.render('Press ESC to exit', False, (GREEN), (0, 0, 0))
            text3 = font.render('Press ENTER to play again', False, (GREEN), (0, 0, 0))

            screen.blit(text1, (50, 200))
            screen.blit(text2, (50, 270))
            screen.blit(text3, (50, 320))

            pygame.display.update()


    def render_settings_view(self, screen, snake):
        font = pygame.font.SysFont('dejavuserif', 30, True, True)
        flag = True
        colors0 = {
            'Green' : GREEN,
            'Yellow' : YELLOW,
            'White' : WHITE,
            'Red' : RED,
            'Blue' : BLUE}
        colors = list(colors0.keys())

        texts = [
            font.render(colors[0], False, YELLOW, (0, 0, 0)),
            font.render(colors[1], False, WHITE, (0, 0, 0)),
            font.render(colors[2], False, WHITE, (0, 0, 0)),
            font.render(colors[3], False, WHITE, (0, 0, 0)),
            font.render(colors[4], False, WHITE, (0, 0, 0))]
        current_highlighted = 0

        while flag:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        flag = False
                        colors_values = list(colors0.values())
                        snake.tail_img.fill(colors_values[current_highlighted])

                    elif event.key == pygame.K_ESCAPE:
                        flag = False

                    elif event.key == pygame.K_UP and current_highlighted > 0:
                        current_highlighted -= 1
                        texts[current_highlighted] = font.render(colors[current_highlighted], False, YELLOW, (0, 0, 0))
                        texts[current_highlighted+1] = font.render(colors[current_highlighted+1], False, WHITE, (0, 0, 0))

                    elif event.key == pygame.K_DOWN and current_highlighted < 4:
                        current_highlighted += 1
                        texts[current_highlighted] = font.render(colors[current_highlighted], False, YELLOW, (0, 0, 0))
                        texts[current_highlighted-1] = font.render(colors[current_highlighted-1], False, WHITE, (0, 0, 0))


            screen.fill((0, 0, 0))
            advise1 = font.render('Select snake color:', False, ((255, 255, 255)), (0, 0, 0))
            advise2 = font.render('Press ENTER to confirm', False, ((255, 255, 255)), (0, 0, 0))

            screen.blit(advise1, (20, 40))
            screen.blit(advise2, (20,400))
            height = 130
            for text in range(len(texts)):
                screen.blit(texts[text], (20, height))
                height+=50

            pygame.display.flip()

        screen.fill((0, 0, 0))
        pygame.display.flip()