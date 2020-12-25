import pygame, random, os
from apple import Apple
from snake import Snake
from game import Game

pygame.init()
pygame.font.init()
font = pygame.font.SysFont('dejavuserif', 22, True, True)
(width, height) = (600, 630)
(s_width, s_height) = (30, 30)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

game_over = False
wait = False

clock = pygame.time.Clock()
move_offset = 30

snake = Snake()
apple = Apple()
game = Game()
FPS = 10
apple_collected = False
apple.spawn()
direction = [0, 0]

apple_sprite = pygame.sprite.Group()
apple_sprite.add(apple)

if not game.render_welcome_view(screen, snake):
    pygame.quit()
    exit()

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True

            if event.key == pygame.K_p:
                wait = True

            if event.key == pygame.K_UP and direction != [0, move_offset]:  # equalise Y
                direction = [0, -move_offset]

            elif event.key == pygame.K_DOWN and direction != [0, -move_offset]:  # equalise Y
                direction = [0, move_offset]

            elif event.key == pygame.K_LEFT and direction != [move_offset, 0]:  # equalise X
                direction = [-move_offset, 0]

            elif event.key == pygame.K_RIGHT and direction != [-move_offset, 0]:  # equalise X
                direction = [move_offset, 0]


    text = font.render('Score: {0}'.format(str(snake.score)), False, (0, 0, 0), (255, 255, 255))

    apple_collected = apple.is_apple_collected(snake.rect[0].x, snake.rect[0].y)

    if apple_collected:
        apple.spawn()
        if snake.is_field_busy(1, apple.rect.center[0], apple.rect.center[1]):
            apple.spawn()
        snake.increase()

    snake.move(direction)

    screen.fill((0, 0, 0))
    game.draw_white_rect(screen)
    screen.blit(text, (0, 0))
    apple_sprite.update()
    apple_sprite.draw(screen)
    snake.draw(screen)

    game.draw_frame(screen)
    pygame.display.flip()
    clock.tick(FPS)

    if snake.is_outside_frame():
        game_over = True

    if wait:
        if game.wait():
            game_over = True
        else:
            wait = False
            clock.tick(FPS)

    if snake.is_collision():
        game_over = True

    if game_over:
        game.board.update_leaderboard(snake.score, screen)
        if game.render_exit_view(screen, snake.score):
            game_over = False
            snake = Snake()
            game.render_welcome_view(screen,snake)
            direction = [0, 0]

pygame.quit()
