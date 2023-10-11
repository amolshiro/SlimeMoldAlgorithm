import random

# Define the maze
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 2, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

start = (1, 1)
end = (1, 8)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up


def slime_mold_path(maze, start, end):
    visited = set()
    stack = [(start, [start])]

    while stack:
        position, path = stack.pop()

        # If the current position is the end, return the path
        if position == end:
            return path

        # Otherwise, spread out to neighboring cells
        for d in directions:
            new_position = (position[0] + d[0], position[1] + d[1])

            if (0 <= new_position[0] < len(maze) and
                    0 <= new_position[1] < len(maze[0]) and
                    maze[new_position[0]][new_position[1]] in [0, 2] and
                    new_position not in visited):

                # Retract from dead ends
                if new_position not in path:
                    new_path = path + [new_position]
                    stack.append((new_position, new_path))
                    visited.add(new_position)

                # If we've reached the end, stop spreading in this direction
                if new_position == end:
                    return new_path

    return None


print(slime_mold_path(maze, start, end))