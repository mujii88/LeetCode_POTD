# 3532. Path Existence Queries in a Graph I

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], max_Diff: int, queries: List[List[int]]) -> List[bool]:
        res=[]
        n=len(nums)
        is_bad=[0]*n
        for i in range(1,n):
            is_bd=1 if abs(nums[i]-nums[i-1])>max_Diff else 0
            is_bad[i]=is_bad[i-1]+is_bd
        for u,v in queries:
            low=min(u,v)
            high=max(u,v)

            temp=is_bad[high]-is_bad[low]
            res.append(temp==0)
        return res


        