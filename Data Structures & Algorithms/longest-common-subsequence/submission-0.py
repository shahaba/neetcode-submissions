class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        cache = {}

        def dfs(i, j):
            if i == n or j == m:
                return 0
            if (i, j) in cache:
                return cache[(i, j)]

            length = 0
            if text1[i] == text2[j]:
                length = 1 + dfs(i + 1, j + 1)
            else:
                length = max(dfs(i + 1, j), dfs(i, j + 1))

            cache[(i, j)] = length

            return cache[(i, j)]

        return dfs(0, 0)