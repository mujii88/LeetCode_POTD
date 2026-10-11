# 3286. Find a Safe Walk Through a Grid

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m=len(grid)
        n=len(grid[0])
        visited=set()
        visited.add((0,0))
        health = health if grid[0][0]==0 else health-1
        dr=[(0,1),(1,0),(0,-1),(-1,0)]

        @lru_cache(None)
        def solve(i,j,health):
            if i==m-1 and j==n-1:
                if health>=1:
                    return True
                return False

            if health==0:
                return False

            
            ans=False
            for row,col in dr:
                new_row,new_col=row+i,col+j
                if 0<=new_row<m and 0<=new_col<n and (new_row,new_col) not in visited:
                    visited.add((new_row,new_col))
                    if grid[new_row][new_col]==1:
                        new_health=health-1
                    else:
                        new_health=health
                    
                    ans=ans or solve(new_row,new_col,new_health)
                    visited.remove((new_row,new_col))
            
            return ans

        return solve(0,0,health)
