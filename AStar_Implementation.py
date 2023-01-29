# A* search
# Inteligencia Artificial
# Mario de Leon 19019

from Reader import *
from Framework import *
from heapq import *
import pygame
import sys


# Find element in nested list START
# https://stackoverflow.com/questions/33938488/finding-the-index-of-an-element-in-nested-lists-in-python
def findRed(list, char):
    for subList in list:
        if char in subList:
            return (subList.index(char), list.index(subList))
    raise ValueError("'{char}' is not in list".format(char=char))


# Find element in nested list and replace it
# https://stackoverflow.com/questions/51318249/python-how-do-i-replace-value-in-a-nested-list
def replaceColor(list, char):
    for subList in list:
        if char in subList:
            sublistIndex = subList.index(char)
            listIndex = list.index(subList)
            list[listIndex][sublistIndex] = 0
            return list
    raise ValueError("'{char}' is not in list".format(char=char))


# Get rectangle based on MAP_SIZE
def getRect(x, y):
    return x * MAP_SIZE + 1, y * MAP_SIZE + 1, MAP_SIZE - 2, MAP_SIZE - 2


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
    return [(grid[y + dy][x + dx], (x + dx, y + dy)) for dx, dy in movement if nextNodeCheck(x + dx, y + dy)]


# Get goal based on mouseclick
def getGoal():
    x, y = pygame.mouse.get_pos()
    gX, gY = x // MAP_SIZE, y // MAP_SIZE
    pygame.draw.rect(win, pygame.Color('green'), getRect(gX, gY))
    click = pygame.mouse.get_pressed()
    if click[0]:
        return (gX, gY)


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
pygame.display.set_caption('A* Algorithm')
# Set window
win = pygame.display.set_mode((SCREEN_HEIGHT*MAP_SIZE, SCREEN_WIDTH*MAP_SIZE))
# Timer
clock = pygame.time.Clock()

try:
    start = findRed(pixels, 2)
except:
    print("No hay punto de inicio.")
try:
    grid = replaceColor(pixels, 2)
except:
    print("El punto de inicio no ha sido encontrado.")
try:
    grid = replaceColor(pixels, 3)
except:
    pass

valuesGrid = grid
valuesGrid = AStarType.stepCost(valuesGrid, 0)
valuesGrid = AStarType.maxValues(valuesGrid, 1)

# Dictionary of lists in grid
dictionary = {}
for y, row in enumerate(grid):
    for x, col in enumerate(row):
        dictionary[(x, y)] = dictionary.get((x, y), []) + nextNodes(x, y)


# A* variables
# Recordatorio para despues: 2 en pixels = rojo
goal = start
visited = {start: None}

# Set map.bmp as background with value grid on top
background = pygame.image.load("map.bmp").convert()
background = pygame.transform.scale(
    background, (SCREEN_HEIGHT * MAP_SIZE, SCREEN_WIDTH * MAP_SIZE))

while True:
    # Escape condition
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    # Draw 2D map
    # Fill window
    win.blit(background, (0, 0))
    # Draw pixels
    # BFS to goal
    mouse = getGoal()
    if mouse and not grid[mouse[1]][mouse[0]]:
        visited = AStarType.solve(start, mouse, dictionary)
        goal = mouse

    # Draw path in real time
    head, segment = goal, goal
    while segment:
        pygame.draw.rect(win, pygame.Color('magenta'), getRect(
            *segment), MAP_SIZE, border_radius=0)
        segment = visited[segment]
    pygame.draw.rect(win, pygame.Color('green'), getRect(
        *head), border_radius=0)
    pygame.draw.rect(win, pygame.Color('red'), getRect(
        *start), border_radius=0)
    # Update display
    pygame.display.flip()
    # Set FPS
    clock.tick(60)
