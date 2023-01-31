# Breadth first search
# Inteligencia Artificial
# Mario de Leon 19019

from Reader import *
from Framework import *
import pygame
import sys
import math
from collections import deque


# Get rectangle based on MAP_SIZE
def getRect(x, y):
    return x * MAP_SIZE + 1, y * MAP_SIZE + 1, MAP_SIZE, MAP_SIZE


# Get goal based on mouseclick
def getGoal():
    x, y = pygame.mouse.get_pos()
    gX, gY = x // MAP_SIZE, y // MAP_SIZE
    pygame.draw.rect(win, pygame.Color('green'), getRect(gX, gY))
    click = pygame.mouse.get_pressed()
    if click[0]:
        return (gX, gY)


def nextNodes(x, y):
    # Check next nodes in nested function
    def nextNodeCheck(x, y):
        if 0 <= x < SCREEN_HEIGHT and 0 <= y < SCREEN_WIDTH and not grid[y][x]:
            return True
        else:
            return False
    # Movement = right, left, up, down, diagonal: north east, north west, south east, south west
    movement = [1, 0], [-1, 0], [0,
                                 1], [0, -1], [1, 1], [-1, 1], [1, -1], [-1, -1]
    return [(x + dx, y + dy) for dx, dy in movement if nextNodeCheck(x + dx, y + dy)]


# Screen variables
SCREEN_HEIGHT = 100
SCREEN_WIDTH = 100
MAP_SIZE = 10

# Load image source
img = Reader(SCREEN_HEIGHT, SCREEN_WIDTH, "maze.PNG")
pixels = img.transformer()

# init pygame
pygame.init
# Title
pygame.display.set_caption('Breadth First Algorithm')
# Set window
win = pygame.display.set_mode((SCREEN_HEIGHT*MAP_SIZE, SCREEN_WIDTH*MAP_SIZE))
# Timer
clock = pygame.time.Clock()

try:
    start = BreadthFirstType.findRed(pixels, 2)
except:
    print("No hay punto de inicio.")
try:
    grid = BreadthFirstType.replaceColor(pixels, 2)
except:
    print("El punto de inicio no ha sido encontrado.")
try:
    grid = BreadthFirstType.replaceColor(pixels, 3)
except:
    pass

# Dictionary of lists in grid
dictionary = {}
for y, row in enumerate(grid):
    for x, col in enumerate(row):
        if not col:
            dictionary[(x, y)] = dictionary.get((x, y), []) + nextNodes(x, y)


# BFS variables
# Recordatorio para despues: 2 en pixels = rojo
goal = start
visited = {start: None}

while True:
    # Escape condition
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    # Draw 2D map
    # Fill window
    win.fill(pygame.Color('white'))
    # Draw pixels
    [[pygame.draw.rect(win, pygame.Color('black'), getRect(x, y))
      for x, col in enumerate(row) if col] for y, row in enumerate(grid)]
    # DFS to goal
    mouse = getGoal()
    if mouse and not grid[mouse[1]][mouse[0]]:
        queue, visited = DepthFirstType.solve(start, mouse, dictionary)
        goal = mouse
    # Draw path in real time
    head, segment = goal, goal
    while head and segment in visited:
        pygame.draw.rect(win, pygame.Color('magenta'), getRect(
            *segment), MAP_SIZE)
        segment = visited[segment]
    pygame.draw.rect(win, pygame.Color('green'), getRect(
        *head))
    pygame.draw.rect(win, pygame.Color('red'), getRect(
        *start))

    # Update display
    pygame.display.flip()
    # Set FPS
    clock.tick(60)
