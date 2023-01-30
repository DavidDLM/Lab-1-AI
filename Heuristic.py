# Heuristic
# Inteligencia Artificial
# Mario de Leon 19019

from scipy.spatial.distance import hamming


# Manhattan distance: sum of horizontal and vertical distances between points
def manhattan(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


# Hamming distance: sum of corresponding elements that differ between vectors
def hamming(x, y):
    return hamming(x, y) * len(x)
