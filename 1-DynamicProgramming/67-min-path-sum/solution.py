import pprint

class Solution:
    def minPathSum(self, grid, debug=False) -> int:
        n, m = len(grid), len(grid[0])
        pp = pprint.PrettyPrinter()
        if debug:
            print("Before processing")
            pp.pprint(grid)
        for i in range(1, n):
            grid[i][0] += grid[i - 1][0]
        if debug:
            print("After processing first column")
            pp.pprint(grid)
        for j in range(1, m):
            grid[0][j] += grid[0][j - 1]
        if debug:
            print("After processing first row")
            pp.pprint(grid)
        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
            if print("After processing the rest")
        pp.pprint(grid)
        return grid[n - 1][m - 1]
