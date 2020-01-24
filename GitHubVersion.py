# A simple self moving cell test

import pygame
import random

# General settings
width = 1280    # Screen with
height = 720    # Screen height

initx = 640     # Cell x stating position
inity = 360     # Cell y stating position

xpos = initx    # x position
ypos = inity    # y position

display = width, height
blue = 0, 0, 255
red = 255, 0, 0
green = 0, 255, 0
length = 20     # dimensions of cell

window = pygame.display.set_mode(display)
pygame.display.set_caption("Cell")

run = True


class Cell:

    def __init__(self, colour,  x, y, length):
        self.x = x
        self.y = y
        self.colour = colour
        self.length = length


# concept for movement:
# It just works
# Have initial conditions, after that have a random range from -10 to 10


def randx():
    ranx = random.randrange(-10, 11)
    Cell.x = xpos
    Cell.x = Cell.x + ranx
    return Cell.x


def randy():
    rany = random.randrange(-10, 11)
    Cell.y = ypos
    Cell.y = Cell.y + rany
    return Cell.y

# colour Cube or colourC


def blueC():
    pygame.draw.rect(window, blue, (randx(), randy(), length, length))
    print(xpos, ypos)


def redC():
    pygame.draw.rect(window, red, (randx(), randy(), 20, 20))


def greenC():
    pygame.draw.rect(window, green, (randx(), randy(), 20, 20))


while run is True:  # Main loop, it just works
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    window.fill((100, 100, 100))
    pygame.draw.rect(window, red, (640, 360, 10, 10))
    blueC()
    xpos = Cell.x
    ypos = Cell.y
    pygame.display.update()
    pygame.time.delay(100)  # Delete if you want a seizure