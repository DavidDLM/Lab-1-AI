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

    def findRed(this, l, c):
        pass

    def replaceColor(this, l, c):
        pass

    def solve(this, s, g, m):
        pass


# BFS Class
class BreadthFirstType(Framework):
    def __init__(this, graph):
        super().__init__(graph)

    # Find element in nested list START
    # https://stackoverflow.com/questions/33938488/finding-the-index-of-an-element-in-nested-lists-in-python
    def findRed(list, char):
        for subList in list:
            if char in subList:
                return (subList.index(char), list.index(subList))
        raise ValueError("'{char}' is not in list".format(char=char))

    def findGreen(list, char):
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


# DFS Class
class DepthFirstType(Framework):
    def __init__(this, graph):
        super().__init__(graph)

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

    # DFS Algorithm
    # https://favtutor.com/blogs/depth-first-search-python
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
            for char in subList:
                if char == 0:
                    sublistIndex = subList.index(char)
                    listIndex = list.index(subList)
                    list[listIndex][sublistIndex] = random.randint(1, 7)
                else:
                    pass
        return list

    # Max values for steps
    def maxValues(list, char):
        for subList in list:
            for char in subList:
                if char == 1:
                    sublistIndex = subList.index(char)
                    listIndex = list.index(subList)
                    list[listIndex][sublistIndex] = 100
                else:
                    pass
        return list

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

    def goalClick(list, gX, gY):
        for subList in list:
            sublistIndex = subList.index(gX)
            listIndex = list.index(gY)
            list[listIndex][sublistIndex] = 0
        return list

    # A* Algorithm
    # https://www.askpython.com/python/examples/a-star-algorithm
    # Parameters: start: starting point, goal: end point, map: graph obtained from Task 1.1

    def solve(start, goal, map):
        queue = []
        heappush(queue, (0, start))
        costVisited = {start: 0}
        visited = {start: None}

        while queue:
            currentCost, currentNode = heappop(queue)
            if currentNode == goal:
                break

            nextNodes = map[currentNode]
            for nextNode in nextNodes:
                nCost, nNode = nextNode
                newCost = costVisited[currentNode] + nCost

                if nNode not in costVisited or newCost < costVisited[nNode]:
                    priority = newCost + manhattan(nNode, goal)
                    heappush(queue, (priority, nNode))
                    costVisited[nNode] = newCost
                    visited[nNode] = currentNode
        return visited
