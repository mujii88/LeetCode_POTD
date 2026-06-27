# 3020. Find the Maximum Number of Elements in Subset

# Here is My sumbission link You can see i explained the approach i used: 
#     https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/solutions/8360930/easiest-solution-with-bes-edge-case-hand-


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freq=Counter(nums)
        ans=1
        if 1 in freq:
            ans=freq[1] if freq[1]%2==1 else freq[1]-1
        for i in set(nums):
            if i==1:
                continue
            curr=i
            count=1
            while freq[math.sqrt(curr)]>=2: 
                count+=2
                curr=math.sqrt(curr)
            ans=max(ans,count)
        
        return ans 

        