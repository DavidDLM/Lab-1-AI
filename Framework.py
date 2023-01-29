# Framework class
# Object Oriented Programming
# Inteligencia Artificial
# Mario de Leon 19019

from collections import deque
from heapq import heappop, heappush
import random
from Heuristic import *


class Framework:
    def __init__(this, graph):
        this.graph = graph
        this.solved = False

    def actions(this, s):
        pass

    def stepCost(this, l, c):
        pass

    def solve(this, s, g, m):
        pass


# BFS Class
class BreadthFirstType(Framework):
    def __init__(this, graph):
        super().__init__(graph)

    # BFS Algorithm
    # https://favtutor.com/blogs/breadth-first-search-python
    # Parameters: start: starting point, goal: end point, map: graph obtained from Task 1.1
    def solve(start, goal, map):
        queue = deque([start])
        visited = {start: None}

        while queue:
            currentNode = queue.popleft()
            if currentNode == goal:
                break

            nextNodes = map[currentNode]
            for nextNode in nextNodes:
                if nextNode not in visited:
                    queue.append(nextNode)
                    visited[nextNode] = currentNode
        return queue, visited


# A* Class
class AStarType(Framework):
    def __init__(this, graph):
        super().__init__(graph)

    # Random values for steps
    def stepCost(list, char):
        for subList in list:
            if char in subList:
                sublistIndex = subList.index(char)
                listIndex = list.index(subList)
                list[listIndex][sublistIndex] = random.randint(1, 7)
                return list
        raise ValueError("'{char}' is not in list".format(char=char))

    # Max values for steps

    def maxValues(list, char):
        for subList in list:
            if char in subList:
                sublistIndex = subList.index(char)
                listIndex = list.index(subList)
                list[listIndex][sublistIndex] = 100
                return list
        raise ValueError("'{char}' is not in list".format(char=char))

    # A* Algorithm
    # https://www.askpython.com/python/examples/a-star-algorithm
    # Parameters: start: starting point, goal: end point, map: graph obtained from Task 1.1
    def solve(start, goal, map):
        queue = []
        heappush(queue, (0, start))
        visited = {start: None}
        costVisit = {start: 0}
        while queue:
            currentCost, currentNode = heappop(queue)
            if currentNode == goal:
                break
            afterNodes = map[currentNode]
            for nextNode in afterNodes:
                newCost, newNode = nextNode
                Cost2 = costVisit[currentNode] + newCost

                if newNode not in costVisit or Cost2 < costVisit[newNode]:
                    priority = newCost + manhattan(newNode, goal)
                    heappush(queue, (priority, newNode))
                    costVisit[newNode] = Cost2
                    visited[newNode] = currentNode
        return visited
