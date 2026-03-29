"""
Given an m x n grid consisting of 1s (land) and 0s (water),
return the number of islands. An island is formed by connecting
adjacent 1s vertically or horizontally
"""

def count_number_of_islands(grid: list[list[int]]) -> int:
    num_rows = len(grid)
    num_cols = len(grid[0])

    def get_neighbors(coord):
        res = []
        row, col = coord
        # Note that delta row and delta col have these values because we want to extract
        # (-1, 0), (0, 1), (1, 0), (0, -1). These are not random.
        delta_row = [-1, 0, 1, 0]
        delta_col = [0, 1, 0, -1]
        for i in range(len(delta_row)):
            r = row + delta_row[i]
            c = col + delta_col[i]
            if 0 <= r < num_rows and 0 <= c < num_cols:
                res.append((r, c))
        return res

    def dfs(coord):
        r, c = coord
        if grid[r][c] == 0:
            return
        grid[r][c] = 0 # sink this island so we don't come back to it again
        for neighbor in get_neighbors(coord):
            nr, nc = neighbor
            if grid[nr][nc] == 1:
                dfs(neighbor)

    count = 0
    for r in range(num_rows):
        for c in range(num_cols):
            if grid[r][c] == 1:
                dfs((r, c))
                # This count is accurate because all of the 1s will be sunk per dfs
                # This will update in real time
                count += 1
    return count
thou