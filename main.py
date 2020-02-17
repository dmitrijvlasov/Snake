import pygame, sys

pygame.init()

size = SCREEN_WIDTH, SCREEN_HEIGHT = 320, 240  # size of display
BLUE = 0, 0, 255  # Color of display
RED = 255, 0, 0  # Color of box (square or rectangle)
box = pygame.Rect(160, 120, 10, 10)  # give coordinates to square

SPEED_X = 5
SPEED_Y = 5

screen = pygame.display.set_mode(size)  # create window

while True:  # loop
    screen.fill(BLUE)  # background blue
    pygame.draw.rect(screen, RED, box)  # create a square
    pygame.display.flip()  # update screen

    for event in pygame.event.get():  # get the list of events
        print(event)
        if event.type == pygame.QUIT:  # if in the list there is event QUIT
            print("Breaking from loop")
            sys.exit()  # then close the window

        if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:  # if in the list there is RIGHT
            print("Moving right")
            if box.x + box.width >= SCREEN_WIDTH:
                pass  # do not move, you have reached the end
            else:
                box.move_ip(SPEED_X, 0)  # then move square

        if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:  # if in the list there is LEFT
            print("Moving left")
            if box.x <= 0:
                pass  # do not move, you have reached the end
            else:
                box.move_ip(-SPEED_X, 0)  # then move square

        if event.type == pygame.KEYUP and event.key == pygame.K_UP:  # if in the list there is UP
            print("Moving up")
            if box.y <= 0:
                pass  # do not move, you have reached the end
            else:
                box.move_ip(0, -SPEED_Y)  # then move square

        if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:  # if in the list there is DOWN
            print("Moving down")
            if box.y + box.height >= SCREEN_HEIGHT:
                pass  # do not move, you have reached the end
            else:
                box.move_ip(0, SPEED_Y)  # then move square
