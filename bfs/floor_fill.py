from collections import deque


def flood_fill(x: int, y: int, replacement: int, image: list[list[int]]) -> list[list[int]]:
    """
    In computer graphics, an uncompressed raster image is presented as a matrix of numbers.
    Each entry of the matrix represents the color of a pixel. A flood fill algorithm
    takes a coordinate r, c and replacement color, and replaces all pixels connected to r, c
    that have the same color. Think paint bucket tool

    e.g.
    0 1 3 4 1
    3 8 8 3 3
    6 7 8 8 3
    12 2 8 9 1
    12 3 1 3 2

    turns into
    0 1 3 4 1
    3 9 9 3 3
    6 7 9 9 3
    12 2 9 9 1
    12 3 1 3 2
    """
    num_rows, num_cols = len(image), len(image[0])
    def get_neighbors(coord, color):
        x, y = coord
        delta_x = [-1, 0, 1, 0]
        delta_y = [0, 1, 0, -1]
        for i in range(len(delta_x)):
            neighbor_x = x + delta_x[i]
            neighbor_y = y + delta_y[i]
            if 0 <= neighbor_x < num_rows and 0 <= neighbor_y < num_cols:
                if image[neighbor_x][neighbor_y] == color:
                    yield neighbor_x, neighbor_y

    def bfs(root):
        queue = deque([root])
        visited = [[False for c in range(num_cols)] for r in range(num_rows)]
        r, c = root
        color = image[r][c]
        image[r][c] = replacement
        visited[r][c] = True
        while len(queue) > 0:
            node = queue.popleft()
            for neighbor in get_neighbors(node, color):
                r, c = neighbor
                if visited[r][c]:
                    continue
                image[r][c] = replacement
                queue.append(neighbor)
                visited[r][c] = True
    bfs((x, y))
    return image
