# 1288. Remove Covered Intervals

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        remaining=len(intervals)
        for i in range(len(intervals)):
            a,b=intervals[i]
            for j in range(len(intervals)):
                if j!=i:
                    c,d=intervals[j]
                    if c<=a and b<=d:
                        remaining-=1
                        break
        
        return remaining
        
    

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        remaining=len(intervals)
        seen=set()
        for i in range(len(intervals)):
            a,b=intervals[i]
            for j in range(len(intervals)):
                if j!=i:
                    c,d=intervals[j]
                    if c<=a and b<=d:
                        if (a,b) not in seen:
                            remaining-=1
                            seen.add((a,b))
                      
        
        return remaining
        