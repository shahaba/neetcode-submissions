class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m, n
        cache = [[0] * COLS for row in range(ROWS)]

        def dfs(r, c):
            if r == ROWS or c == COLS:
                return 0
            if cache[r][c] > 0:
                return cache[r][c]
            if r == ROWS - 1 and c == COLS - 1:
                return 1

            cache[r][c] = dfs(r + 1, c) + dfs(r, c + 1)

            return cache[r][c]

        return dfs(0, 0)

