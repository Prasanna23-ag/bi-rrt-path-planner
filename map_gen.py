import numpy as np
import cv2

# Define map size similar to Umaze (e.g., 100x100 pixels)
map_size = (100, 100)
map_img = np.ones(map_size, dtype=np.uint8) * 255  # white = free space

# Draw border (black edges)
cv2.rectangle(map_img, (0, 0), (map_size[1]-1, map_size[0]-1), 0, thickness=2)

# Define center point
center_x, center_y = map_size[1] // 2, map_size[0] // 2

# Draw thick L-shaped obstacle
# Vertical part of L
cv2.rectangle(map_img, (center_x - 4, center_y - 20), (center_x + 4, center_y + 20), 0, -1)
# Horizontal part of L
cv2.rectangle(map_img, (center_x + 4, center_y + 12), (center_x + 30, center_y + 20), 0, -1)

# Save as PGM
cv2.imwrite("custom_map.pgm", map_img)
print("Compact Umaze-style map saved as custom_map.pgm")
