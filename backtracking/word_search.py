"""
Given an m x n board of characters and a word, return True if the worst exists
in the grid. The word can be constructed from letters in adjacent cells but cannot
reuse the same letter cell more than once
"""

def exist(board: list[list[str]], word: str) -> bool:
    def dfs(i, j, word_i):
        # pruning
        if board[i][j] != word[word_i]:
            return False
        # base case
        if word_i == len(word) - 1:
            return True
        char = board[i][j]
        board[i][j] = "*" # already used
        coors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        for r, c in coors:
            if 0 <= r < len(board) and 0 <= c < len(board[0]):
                if dfs(r, c, word_i + 1):
                    return True
        board[i][j] = char
        return False

    for r in range(len(board)):
        for c in range(len(board[0])):
            if dfs(r, c, 0):
                return True
    return Falsetho
