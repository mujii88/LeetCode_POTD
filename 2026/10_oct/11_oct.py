# 2778. Sum of Squares of Special Elements 

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        ans=0
        n=len(nums)
        for i in range(1,len(nums)+1):
            if n%i==0:
                ans+=(nums[i-1]**2)
        return ans
