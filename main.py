import pygame, sys

pygame.init()

size = SCREEN_WIDTH, SCREEN_HEIGHT = 320, 240  # size of display
BLUE = 0, 0, 255  # Color of display
RED = 255, 0, 0  # Color of box (square or rectangle)
box = pygame.Rect(160, 120, 10, 10)  # give coordinates to square
FPS = 30
SPEED_X = 5
SPEED_Y = 1
move_down = False
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

        # if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:  # if in the list there is RIGHT
        #     pressed_right = True
        #     print("Moving right")
        #     if box.x + box.width >= SCREEN_WIDTH:
        #         pass  # do not move, you have reached the end
        #     else:
        #         box.move_ip(SPEED_X, 0)  # then move square
        # # if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:  # if in the list there is RIGHT
        # #     pressed_right = False
        #
        # if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:  # if in the list there is LEFT
        #     print("Moving left")
        #     if box.x <= 0:
        #         pass  # do not move, you have reached the end
        #     else:
        #         box.move_ip(-SPEED_X, 0)  # then move square
        #
        # if event.type == pygame.KEYUP and event.key == pygame.K_UP:  # if in the list there is UP
        #     print("Moving up")
        #     if box.y <= 0:
        #         pass  # do not move, you have reached the end
        #     else:
        #         box.move_ip(0, -SPEED_Y)  # then move square
        #
        # if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:  # if in the list there is DOWN
        #     print("Moving down")
        #     if box.y + box.height >= SCREEN_HEIGHT:
        #         pass  # do not move, you have reached the end
        #     else:
        #         box.move_ip(0, SPEED_Y)  # then move square

        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:  # if in the list there is DOWN
            print('button pressed')
            move_down = True
        if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:  # if in the list there is DOWN
            print('button released')
            move_down = False

    if move_down is True:
        print('start moving')
        box.move_ip(0, SPEED_Y)

    pygame.time.Clock().tick(FPS)
"""
while True:
    for event in events:
        if button_down:
            activate = True
        if button_up:
            activate = False

    if activate is True:
        move()
"""
