import heapq
from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        busy = []  # Min-heap storing (free_time, server_id)
        free = SortedList(range(k))  # Sorted set of available server IDs
        request_count = [0] * k
        
        for i, (t, l) in enumerate(zip(arrival, load)):
            # 1. Free up all servers that have finished by time t
            while busy and busy[0][0] <= t:
                _, server_id = heapq.heappop(busy)
                free.add(server_id)
                
            # 2. If all servers are busy, drop the request
            if not free:
                continue
                
            # 3. Binary search for the first server >= (i % k)
            idx = free.bisect_left(i % k)
            
            # Wrap around to the smallest available server if none >= (i % k)
            if idx == len(free):
                idx = 0
                
            # 4. Assign the request and mark server as busy
            assigned_server = free.pop(idx)
            request_count[assigned_server] += 1
            heapq.heappush(busy, (t + l, assigned_server))
            
        max_reqs = max(request_count)
        return [server for server, count in enumerate(request_count) if count == max_reqs]

# 1606. Find Servers That Handled Most Number of Requests
