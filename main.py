import pygame
import random

# Game Constants
pygame.init()
red = (255, 0, 0)
green = (0, 155, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
color_list = [red, green, blue]
game_frame_width = 800
game_frame_height = 600
gameDisplay = pygame.display.set_mode((game_frame_width, game_frame_height))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 25)

# Snake Object
height = 10
width = height
block_size = 10

def snake(block_size, snakelist):
    for X_Y in snakelist:
        pygame.draw.rect(gameDisplay, green, [X_Y[0], X_Y[1], block_size, block_size])


def message_to_screen(msg, color, x, y):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [x, y])

def gameLoop():
    FPS = 10
    lead_x = game_frame_width/2
    lead_y = game_frame_height/2
    lead_x_change = 0
    lead_y_change = 0
    snakeList = []
    snakeLenght = 1
    rand_apple_x = round(random.randrange(0, game_frame_width-block_size))#/10.0)*10.0
    rand_apple_y = round(random.randrange(0, game_frame_height-block_size))#/10.0)*10.0
    gameExit = False
    gameOver = False

    while not gameExit:

        # Event Handling
        while gameOver == True:
            gameDisplay.fill(black)
            message_to_screen(msg='Game Over, press c to continue or q to quit.', color=green,
                              x=game_frame_width/3.5, y=game_frame_height/2)
            message_to_screen(msg='Score: {0}'.format((snakeLenght-1)*10), color=green,
                              x=game_frame_width/2.3, y=game_frame_height/1.8)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                gameExit = True

            # When the key is pressed down
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                if event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                if event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                if event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

            # When the key is released
            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            #         lead_x_change = 0
            #     if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            #         lead_y_change = 0

            # Boundaries
                if lead_x >= game_frame_width or lead_x < 0:
                    gameOver = True
                if lead_y >= game_frame_height or lead_y < 0:
                    gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change
        gameDisplay.fill(blue)
        appleThickness = 30
        pygame.draw.rect(gameDisplay, red, [rand_apple_x, rand_apple_y, appleThickness, appleThickness])
        message_to_screen(msg='Score: {0}'.format((snakeLenght-1)*10), color=green, x=700, y=25)

        # Add the length of the snake object
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLenght:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        snake(block_size=block_size, snakelist=snakeList)
        pygame.display.update()

        # if lead_x >= rand_apple_x and lead_x <= rand_apple_x + appleThickness:
        #     if lead_y >= rand_apple_y and lead_y <= rand_apple_y + appleThickness:
        #         rand_apple_x = round(random.randrange(0, game_frame_width-block_size))#/10.0)*10.0
        #         rand_apple_y = round(random.randrange(0, game_frame_height-block_size))#/10.0)*10.0
        #         snakeLenght += 1

        # If the object collides with the apple
        if lead_x > rand_apple_x and lead_x < rand_apple_x + appleThickness or lead_x + block_size\
            > rand_apple_x and lead_x + block_size < rand_apple_x + appleThickness:
            if lead_y > rand_apple_y and lead_y < rand_apple_y + appleThickness or lead_y + block_size\
               > rand_apple_y and lead_y + block_size < rand_apple_y + appleThickness:
                rand_apple_x = round(random.randrange(0, game_frame_width-block_size))#/10.0)*10.0
                rand_apple_y = round(random.randrange(0, game_frame_height-block_size))#/10.0)*10.0
                snakeLenght += 1
            #elif lead_y + block_size > rand_apple_y
    clock.tick(FPS*snakeLenght)

    pygame.quit()
    quit()

gameLoop()
# 1 Display
# 2 Render
# 3 Minus size
# 4 loop

