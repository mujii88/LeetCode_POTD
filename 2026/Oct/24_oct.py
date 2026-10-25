class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        def dfs(r, c):
            # If we go out of bounds, the island touches the edge (not closed)
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return False
            
            # If we hit water (or visited land marked as water), it's a valid boundary
            if grid[r][c] == 1:
                return True
            
            # Mark the current land as visited by turning it into water
            grid[r][c] = 1
            
            # Evaluate all 4 directions FIRST to prevent short-circuiting
            up = dfs(r - 1, c)
            down = dfs(r + 1, c)
            left = dfs(r, c - 1)
            right = dfs(r, c + 1)
            
            # Return True only if all directions are bounded by water
            return up and down and left and right

        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                # Start a DFS only if we find unvisited land
                if grid[r][c] == 0:
                    if dfs(r, c):
                        count += 1
                        
        return count
