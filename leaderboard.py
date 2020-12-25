import pygame, os
GREEN = (0, 255, 0)

class Leaderboard:

    high_scores = []
    names = []

    def __init__(self):
        if not os.path.isfile("leaderboard.txt"):
            self.reset()
        else:
            self.file = open("leaderboard.txt", "r")
            i = 0
            for line in self.file:
                self.names.append("")
                self.high_scores.append(0)
                num, self.names[i], self.high_scores[i] = line.split()
                i += 1

    def reset(self):
        self.file = open("leaderboard.txt", "w+")
        size = len(self.high_scores)

        for i in range(5):
            if size == 0:
                self.high_scores.append(0)
                self.names.append('............')
            else:
                self.high_scores[i] = 0
                self.names[i] = '............'
            self.file.write(str(i + 1) + ". " + str(self.names[i]) + " " + str(self.high_scores[i]) + "\n")

        self.file.close()

    def check_high_score(self, points):
        size = len(self.high_scores)
        if points > int(self.high_scores[size-1]):
            return True
        else:
            return False

    def save_leaderboard_to_file(self):
        self.file = open("leaderboard.txt", "w+")
        for i in range(len(self.high_scores)):
            self.file.write(str(i + 1) + ". " + str(self.names[i]) + " " + str(self.high_scores[i]) + "\n")
        self.file.close()

    def update_leaderboard(self, points, screen):
        if self.check_high_score(points):
            name = self.render_text_window(screen)
            size = len(self.high_scores)
            self.high_scores[size-1] = points
            self.names[size-1] = name

            for i in range(size-1, 0, -1):
                if int(self.high_scores[i-1]) < int(self.high_scores[i]):
                    temporary_score = self.high_scores[i-1]
                    temporary_name = self.names[i-1]
                    self.high_scores[i-1] = self.high_scores[i]
                    self.names[i-1] = self.names[i]
                    self.high_scores[i] = temporary_score
                    self.names[i] = temporary_name

            self.save_leaderboard_to_file()

    def render_text_window(self, screen):
        screen.fill((0, 0, 0))
        pygame.display.set_caption('New highscore window')
        font = pygame.font.SysFont('dejavuserif', 22, True, True)
        displayed_text = ''
        flag = True
        while flag:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    flag = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        flag = False

                    elif event.key == pygame.K_RETURN and len(displayed_text) != 0:
                        return displayed_text

                    elif event.key == pygame.K_BACKSPACE:
                        text_length = len(displayed_text)
                        if text_length != 0:
                            displayed_text = displayed_text[0:text_length-1]

                    elif len(displayed_text) < 15 and event.key != pygame.K_RETURN:
                        displayed_text += event.unicode

            screen.fill((0, 0, 0))
            text0 = font.render('New highscore!', False, (GREEN), (0, 0, 0))
            text1 = font.render('Enter your non-empty name:', False, (GREEN), (0, 0, 0))
            to_display = font.render(displayed_text, False, (GREEN), (0, 0, 0))
            text2 = font.render('Press ENTER to confirm', False, (GREEN), (0, 0, 0))
            screen.blit(text0, (20, 50))
            screen.blit(text1, (20, 150))
            screen.blit(to_display, (20, 300))
            screen.blit(text2, (20, 450))

            pygame.display.update()