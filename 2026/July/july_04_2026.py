# 2492. Minimum Score of a Path Between Two Cities


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        visited=set()
        graph=defaultdict(list)
        for a,b,distance in roads:
            graph[a].append((b,distance))
            graph[b].append((a,distance))
        self.ans=float('inf')
        def solve(parent):
            visited.add(parent)
            for child,dist in graph[parent]:
                self.ans=min(self.ans,dist)
                if child not in visited:
                    solve(child)
        solve(1)
        return self.ans
        