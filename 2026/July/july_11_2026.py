# 2685. Count the Number of Complete Components

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        freq=defaultdict(int)
        graph=[[i] for i in range(n)]

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        for node in range(n):
            child=tuple(sorted(graph[node]))
            freq[child]+=1

        total=0
        for key ,val in freq.items():
            if len(key)==val:
                total+=1
        
        return total
        


