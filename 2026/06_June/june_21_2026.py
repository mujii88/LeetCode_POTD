class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count=0
        i=0
        while i<len(costs) and  costs[i]<=coins:
            count+=1
            coins-=costs[i]
            i+=1

        return count        



# 1833. Maximum Ice Cream Bars