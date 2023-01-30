import pygame
from heapq import *
from Reader import *
from Framework import *


def getRect(x, y):
    return x * MAP_SIZE + 1, y * MAP_SIZE + 1, MAP_SIZE - 2, MAP_SIZE - 2


def nextNodes(x, y):
    # Check next nodes in nested function
    def nextNodeCheck(
        x, y): return True if 0 <= x < SCREEN_HEIGHT and 0 <= y < SCREEN_WIDTH else False
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

# init pygame
pygame.init
# Title
pygame.display.set_caption('A* Algorithm')
# Set window
win = pygame.display.set_mode((SCREEN_HEIGHT*MAP_SIZE, SCREEN_WIDTH*MAP_SIZE))
# Timer
clock = pygame.time.Clock()

# Prepare grid
img = Reader(SCREEN_HEIGHT, SCREEN_WIDTH, "maze.PNG")
pixels = img.transformer()
start = AStarType.findRed(pixels, 2)
grid = AStarType.replaceColor(pixels, 2)

try:
    # Replace color green
    grid = AStarType.replaceColor(pixels, 3)
except:
    pass

# Random grid values for A* cost
grid = AStarType.maxValues(grid, 1)
grid = AStarType.stepCost(grid, 0)
# print(grid)

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
    # A* to goal
    mouse = getGoal()
    if mouse:
        visited = AStarType.solve(start, mouse, dictionary)
        goal = mouse

    # Draw path in real time
    segment, head = goal, goal
    while segment and segment in visited:
        pygame.draw.rect(win, pygame.Color('magenta'), getRect(*segment))
        segment = visited[segment]
    pygame.draw.rect(win, pygame.Color('red'), getRect(*start))
    pygame.draw.rect(win, pygame.Color('green'), getRect(*head))

    # Update display
    pygame.display.flip()
    # Set FPS
    clock.tick(60)
