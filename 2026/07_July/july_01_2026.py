class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        dr=[(0,1),(1,0),(0,-1),(-1,0)]
        n=len(grid)
        self.visited=set()
        multi_queue=deque()
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j]==1:
                    grid[i][j]=0
                    self.visited.add((i,j))
                    multi_queue.append((i,j))
                else:
                    grid[i][j]=-1


        # grid boundry checking function
        def isValid(i,j):
            if 0<=i<n and 0<=j<n:
                return True
            return False



        # binary search on answer condition checking funcion
        def isPossible(mid):
            visited=set()
            queue=deque()
            queue.append((0,0))

            if grid[0][0]<mid or grid[n-1][n-1]<mid:
                return False

            while queue:
                sze=len(queue)
                for i in range(sze):
                    curr=queue.popleft()
                    curr_r,curr_c=curr
                    if curr_r==n-1 and curr_c==n-1:
                        return True
                    for row,col in dr:
                        new_r=curr_r+row
                        new_c=curr_c+col
                        if isValid(new_r,new_c) and (new_r,new_c)  not in visited and grid[new_r][new_c]>=mid:
                            visited.add((new_r,new_c)) 
                            queue.append((new_r,new_c))
            
            return False
        

        # this is the implementation of the multi_source BFS algorithm
        while multi_queue:
            size=len(multi_queue)
            for i in range(size):
                curr=multi_queue.popleft()
                curr_r,curr_c=curr
                for row,col in dr:
                    new_r=curr_r+row
                    new_c=curr_c+col
                    if isValid(new_r,new_c) and (new_r,new_c) not in self.visited:
                        self.visited.add((new_r,new_c))
                        grid[new_r][new_c]=grid[curr_r][curr_c]+1
                        multi_queue.append((new_r,new_c))

        
        # Binary Search on Answer for getting the valid answer
        left=0
        right=0
        ans=0
        for i in range(n):
            for j in range(n):
                right=max(right,grid[i][j])

        while left<=right:
            mid=(left+right)//2
            if isPossible(mid):
                ans=mid
                left=mid+1
            else:
                right=mid-1

        
        return ans




