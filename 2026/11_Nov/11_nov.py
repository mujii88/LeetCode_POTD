# 3789. Minimum Cost to Acquire Required Items
class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # 1. For the overlapping amount where we need BOTH items:
        # Either buy them separately (cost1 + cost2) or together (costBoth)
        overlap = min(need1, need2)
        ans = overlap * min(cost1 + cost2, costBoth)
        
        # 2. Subtract the overlap to see what is left over
        need1 -= overlap
        need2 -= overlap
        
        # 3. Fulfill the remaining need1 (if any) using the cheapest option
        ans += need1 * min(cost1, costBoth)
        
        # 4. Fulfill the remaining need2 (if any) using the cheapest option
        ans += need2 * min(cost2, costBoth)
        
        return ans
