from functools import lru_cache

class Solution:
    def pathsWithMaxScore(self, board):
        m = len(board)
        n = len(board[0])
        MOD = 10**9 + 7
        
        # Directions: Right, Down, Down-Right
        dr = [(0, 1), (1, 0), (1, 1)]

        @lru_cache(None)
        def solve(i, j):
            # Base Case: Reached 'S'
            if i == m - 1 and j == n - 1:
                return [0, 1] # [Score of 0, 1 way to be at the start]
            
            best_score = -float('inf')
            total_paths = 0
            
            for row, col in dr:
                new_row = row + i
                new_col = col + j
                
                if 0 <= new_row < m and 0 <= new_col < n and board[new_row][new_col] != "X":
                    val = int(board[new_row][new_col]) if board[new_row][new_col].isdigit() else 0
                    
                    # Ask the neighbor for its [max_score, paths]
                    child_score, child_paths = solve(new_row, new_col)
                    
                    # Calculate the score if we take this route
                    current_score = child_score + val
                    
                    # Did we find a NEW strictly higher score?
                    if current_score > best_score:
                        best_score = current_score
                        total_paths = child_paths # Reset paths to this new best route
                        
                    # Did we TIE the highest score?
                    elif current_score == best_score:
                        total_paths = (total_paths + child_paths) % MOD
            
            return [best_score, total_paths]

        # Start the recursion from 'E' at (0,0)
        max_score, paths = solve(0, 0)
        
        # If 'S' is completely unreachable
        if max_score == -float('inf'):
            return [0, 0]
            
        return [max_score, paths]