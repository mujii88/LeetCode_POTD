# 1260. Shift 2D Grid

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        for ops in range(k):
            new_grid=[[0]*len(grid[0]) for i in range(len(grid))]
            temp=grid[len(grid)-1][len(grid[0])-1]
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if i>0 and j==0:
                        new_grid[i][j]=grid[i-1][len(grid[0])-1]
                    elif j>0:
                        new_grid[i][j]=grid[i][j-1]
            new_grid[0][0]=temp
            grid=new_grid

        return grid

        