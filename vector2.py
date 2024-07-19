import numpy as np


def length(vector2):
    return np.linalg.norm(vector2)


def normalized(vector2):
    return vector2 / length(vector2)
