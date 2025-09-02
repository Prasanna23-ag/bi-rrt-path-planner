import random
from rrt_utils import Node, steer, is_collision, get_nearest, build_path, distance

def bi_rrt(start, goal, map_binary, step_size=5, max_iters=1000, goal_thresh=10):
    height, width = map_binary.shape
    tree_start = [Node(start)]
    tree_goal = [Node(goal)]
    full_path = None

    for _ in range(max_iters):
        rand_point = (random.randint(0, width - 1), random.randint(0, height - 1))

        for tree_a, tree_b in [(tree_start, tree_goal), (tree_goal, tree_start)]:
            nearest = get_nearest(tree_a, rand_point)
            new_point = steer(nearest.point, rand_point, step_size)

            if not is_collision(nearest.point, new_point, map_binary):
                new_node = Node(new_point, nearest)
                tree_a.append(new_node)

                nearest_b = get_nearest(tree_b, new_point)
                if distance(nearest_b.point, new_point) < goal_thresh and not is_collision(nearest_b.point, new_point, map_binary):
                    path_a = build_path(new_node)
                    path_b = build_path(nearest_b)
                    full_path = path_a + path_b[::-1]
                    return full_path
    return None
