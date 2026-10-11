# 1846. Maximum Element After Decreasing and Rearranging

# Detailed Explaination:
                       
                    #https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/solutions/8362486/one-pass-solution-with-o1-space-complexi-nj3p



class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        maxi=1
        if arr[0]!=1:
            arr[0]=1
        
        for i in range(1,len(arr)):
            if arr[i]-arr[i-1]>1:
                arr[i]=arr[i-1]+1
            maxi=max(maxi,arr[i])
        
        return maxi
        
        

        