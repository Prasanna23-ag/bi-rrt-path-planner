import math
import numpy as np

class Node:
    def __init__(self, point, parent=None):
        self.point = point
        self.parent = parent

def distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def steer(from_point, to_point, step_size):
    theta = math.atan2(to_point[1] - from_point[1], to_point[0] - from_point[0])
    return (int(from_point[0] + step_size * math.cos(theta)),
            int(from_point[1] + step_size * math.sin(theta)))

def is_collision(p1, p2, map_binary):
    line = np.linspace(p1, p2, num=10, dtype=int)
    height, width = map_binary.shape
    for x, y in line:
        if x < 0 or y < 0 or x >= width or y >= height or map_binary[y, x] == 1:
            return True
    return False

def get_nearest(tree, point):
    return min(tree, key=lambda node: distance(node.point, point))

def build_path(node):
    path = []
    while node:
        path.append(node.point)
        node = node.parent
    return path[::-1]
