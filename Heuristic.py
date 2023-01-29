# Heuristic
# Inteligencia Artificial
# Mario de Leon 19019

from scipy.spatial.distance import hamming


# Manhattan distance: sum of horizontal and vertical distances between points
def manhattan(x, y):
    return sum(abs(val1-val2) for val1, val2 in zip(x, y))


# Hamming distance: sum of corresponding elements that differ between vectors
def hamming(x, y):
    return hamming(x, y) * len(x)
