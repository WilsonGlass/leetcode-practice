def pacific_atlantic(heights: list[list[int]]) -> list[list[int]]:
    """
    There is an m x n rectangular island that borders both the pacific and atlantic oceans.
    The pacific ocean touches the island's left and top edges and atlantic
    touches the island's right and bottom edges.

    The island is partitioned into a grid of square cells. You are given an m x n
    integer matrix heights where heights[r][c] represents the height above
    sea level of the cell coordinate (r, c)

    The island receives a lot of rain, and the rain water can flow to neighboring
    cells directly north, south, east, and west if the neighboring cell's height is less
    than or equal to the current cell's height. Water can flow from any cell adjacent
    to an ocean into the ocean.

    Return a 2D list of grid coordinates where result[i] = [r_i, c_i] denotes that rain water
    can flow from cell (r_i, c_i) to both the pacific and atlantic oceans.
    """
    if not heights:
        return []
    m, n = len(heights), len(heights[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def dfs(i, j, visited):
        visited.add((i, j))
        for dx, dy in directions:
            x, y = i + dx, j + dy
            if 0 <= x < m and 0 <= y < n:
                if (x, y) not in visited and heights[x][y] >= heights[i][j]:
                    dfs(x, y, visited)

    pacific, atlantic = set(), set()
    for j in range(n): dfs(0, j, pacific)
    for j in range(m): dfs(j, 0, pacific)
    for j in range(n): dfs(m - 1, j, atlantic)
    for i in range(m): dfs(i, n - 1, atlantic)

    # Intersection
    return list(pacific & atlantic)