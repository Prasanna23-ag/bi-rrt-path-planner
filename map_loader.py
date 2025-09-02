import cv2
import numpy as np

def load_map(path, kernel_size=11):
    map_img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    map_binary = (map_img < 250).astype(np.uint8)
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    map_binary = cv2.dilate(map_binary, kernel, iterations=1)
    map_color = cv2.cvtColor(map_img, cv2.COLOR_GRAY2BGR)
    return map_img, map_binary, map_color
