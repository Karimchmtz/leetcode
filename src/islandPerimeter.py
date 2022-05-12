class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        count = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if (grid[i][j] == 0):
                    continue
                if i == 0:
                    count += 1
                if i == len(grid) - 1:
                    count += 1
                if j == 0:
                    count += 1
                if j == len(grid[i]) - 1:
                    count += 1
                if j != 0:
                    if grid[i][j - 1] == 0:
                        count += 1
                if j != len(grid[i]) - 1:
                    if grid[i][j + 1] == 0:
                        count += 1
                if i != 0: 
                    if grid[i - 1][j] == 0:
                        count += 1
                if i != len(grid) - 1:
                    if grid[i + 1][j] == 0:
                        count += 1
        return count