
# 3105. Longest Strictly Increasing or Strictly Decreasing Subarray

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans=1
        count=1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                count+=1
                ans=max(ans,count)
            else:
                
                count=1
        
        
        count=1
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                count+=1
                ans=max(ans,count)
            else:
               
                count=1
            
        return ans
        



                


        
