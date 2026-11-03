class Solution:
    def minMoves(self, nums: List[int]) -> int:

        mini=max(nums)
        ans=0
        for elem in nums:
            ans+=(mini-elem)
        
        return ans
        

# 3736. Minimum Moves to Equal Array Elements III
