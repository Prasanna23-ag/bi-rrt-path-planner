from map_loader import load_map
from planner import bi_rrt
from visualizer import draw_path, save_csv, save_plot

def main():
    map_img, map_binary, map_color = load_map("custom_map.pgm", kernel_size=11)
    start = (10, 10)
    goal = (map_binary.shape[1] - 10, map_binary.shape[0] - 10)

    path = bi_rrt(start, goal, map_binary)

    if path:
        draw_path(map_color, path, start, goal)
        save_csv(path)
        save_plot(path)
    else:
        print("Path not found.")

if __name__ == "__main__":
    main()
