# 3689. Maximum Total Subarray Value I
# Medium


class Solution:
    def maxTotalValue(self, nums, k: int) -> int:
        maxi=max(nums)
        mini=min(nums)
        return (maxi-mini)*k



A=Solution()
print(A.maxTotalValue([4,2,5,1],3))