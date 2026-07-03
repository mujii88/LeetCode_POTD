# 3620. Network Recovery Pathways

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        graph=defaultdict(list)
        l=float('inf')
        r=float('-inf')
        n=len(online)
        for u,v,cost in edges:
            graph[u].append((v,cost))
            l=min(cost,l)
            r=max(r,cost)



        def isValid(mid):
            dist=[float('inf')]*n
            heap=[(0,0)]
            dist[0]=0
            while heap:
                dst,u=heapq.heappop(heap)

                if dst>k:
                    return False
                if u==n-1:
                    return True
                if dst>dist[u]:
                    continue
                
                for v,w in graph[u]:
                    if not online[v] or  w<mid:
                        continue
                    if dist[v]>dist[u]+w:
                        dist[v]=dist[u]+w
                        heapq.heappush(heap,(dist[v],v))

            return False


            

        if not isValid(l):
            return -1
        while l<=r:
            mid=(l+r)//2
            if isValid(mid):
       
                l=mid+1
            else:
                r=mid-1

        return r


        


