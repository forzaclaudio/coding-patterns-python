import copy
import pprint
#grid = [[1]]
#grid = [[1,2], [3,4]]
#grid = [[1,2,3],[4,5,6],[7,8,9]]
#grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#grid = [[1,3,1],[1,5,1],[4,2,1]]
#grid = [[1,2,3],[4,5,6]]
grid = [[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],
       [9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],
       [8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],
       [6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],
       [7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],
       [9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],
       [1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],
       [3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],
       [1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],
       [5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],
       [2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],
       [0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]
class Solution:

    def __init__(self):
        self.mapping = {}

    def generate_costs(self, grid, m, n):
        if not self.mapping.get((m,n)):
            if m == 1 and n ==1:
                return [grid[m-1][n-1]]
            else:
                res = []
                if n > 1:
                    a = self.generate_costs(grid, m, n-1)
                    for i in a:
                        if not isinstance(i, list):
                            i = [i]
                        res.append(sum(i+[grid[m-1][n-1]]))
                if m > 1:
                    b = self.generate_costs(grid, m-1, n)
                    for i in b:
                        if not isinstance(i, list):
                            i = [i]
                        res.append(sum(i+[grid[m-1][n-1]]))
            self.mapping[(m,n)] = res
        return self.mapping.get((m,n))

    def minPathSum(self, grid) -> int:
        n, m = len(grid), len(grid[0])
        pp = pprint.PrettyPrinter()
        print("Before processing")
        pp.pprint(grid)
        for i in range(1, n):
            grid[i][0] += grid[i - 1][0]
        print("After processing first column")
        pp.pprint(grid)
        for j in range(1, m):
            grid[0][j] += grid[0][j - 1]
        print("After processing first row")
        pp.pprint(grid)
        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        print("After processing the rest")
        pp.pprint(grid)
        return grid[n - 1][m - 1]

def generate_paths(grid, m, n):
    if m == 1 and n == 1:
        return [grid[m-1][n-1]]
    else:
        res = []
        if n > 1:
            a = generate_paths(grid, m, n-1)
            for i in a:
                if not isinstance(i, list):
                    i = [i]
                res.append(i + [grid[m-1][n-1]])
        if m > 1:
            b = generate_paths(grid, m - 1, n)
            for i in b:
                if not isinstance(i, list):
                    i = [i]
                res.append(i+[grid[m-1][n-1]])
        return res
if False:
    print(grid)
    paths = generate_paths(grid, len(grid), len(grid[0]))
    print("paths:", paths)
    try:
        costs = [sum(a) for a in paths]
    except:
        costs = paths[0]
    print("costs:", costs)
    if isinstance(costs, list):
        print("winner:", min(costs))
    else:
        print("winner:", costs)
s = Solution()
grid1 = copy.deepcopy(grid)
grid2 = copy.deepcopy(grid)
print("optimal solution:", s.minPathSum(grid1))
if False:
    print(grid2)
    computed_costs = s.generate_costs(grid2, len(grid2), len(grid2[0]))
    print("computed costs:", computed_costs)
    print("winner:", min(computed_costs))

