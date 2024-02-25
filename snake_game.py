import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 640, 480
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Snake initial position and size
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_speed = 15

# Food position
food_pos = [random.randrange(1, (WIDTH//10)) * 10,
            random.randrange(1, (HEIGHT//10)) * 10]
food_spawn = True

# Initial direction
direction = 'RIGHT'
change_to = direction

# Score function
score = 0


# Game Over function
def game_over():

    myFont = pygame.font.SysFont('times new roman', 90)
    GOsurf = myFont.render('Your Score is: ' + str(score), True, RED)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (WIDTH/2, HEIGHT/4)
    win.blit(GOsurf, GOrect)
    pygame.display.flip()
    time.sleep(2)

    pygame.quit()
    quit()


# Main Function
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Validation of direction
    if change_to == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'

    # Update snake position [x, y]
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # Snake Body Growing Mechanism
    # if food and snake collide then scores
    # will be incremented by 10
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 10
        food_spawn = False
    else:
        snake_body.pop()
    if not food_spawn:
        food_pos = [random.randrange(1, (WIDTH//10)) * 10,
                    random.randrange(1, (HEIGHT//10)) * 10]

    food_spawn = True
    win.fill(WHITE)

    for pos in snake_body:
        pygame.draw.rect(win, GREEN,
                         pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(win, RED, pygame.Rect(
        food_pos[0], food_pos[1], 10, 10))

    # Game Over conditions
    if snake_pos[0] < 0 or snake_pos[0] > WIDTH-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > HEIGHT-10:
        game_over()

    # Touching the snake body
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    # displaying score function
    myFont = pygame.font.SysFont('times new roman', 24)
    myFont1 = pygame.font.SysFont('times new roman', 24)
    score_surface = myFont.render('Score: ' + str(score), True, RED)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (WIDTH/2, 10)
    win.blit(score_surface, score_rect)

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refres Rate
    pygame.time.Clock().tick(snake_speed)
