import cv2
import csv
import matplotlib.pyplot as plt

def draw_path(map_color, path, start, goal):
    for i in range(1, len(path)):
        cv2.line(map_color, path[i-1], path[i], (0, 0, 255), thickness=2)
    cv2.circle(map_color, start, 5, (0, 255, 0), -1)
    cv2.circle(map_color, goal, 5, (255, 0, 0), -1)
    cv2.imshow("Bi-RRT Path", map_color)
    cv2.waitKey(0)
    cv2.imwrite("saved_path_with_map.png", map_color)

def save_csv(path, filename="saved_path.csv"):
    with open(filename, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["x", "y"])
        for p in path:
            writer.writerow([p[0], p[1]])

def save_plot(path, filename="saved_path_plot.png"):
    xs, ys = zip(*path)
    plt.figure(figsize=(15, 15), dpi=150)
    plt.plot(xs, ys, marker='o', color='blue', linewidth=2)
    plt.title("Bi-RRT Path")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.savefig(filename)
    plt.close()
