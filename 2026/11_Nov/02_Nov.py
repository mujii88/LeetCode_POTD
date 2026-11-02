class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n, cnt = len(nums), 0
        nums.sort()
        x = nums[n // 2]
        for i in range(n):
            cnt += abs(nums[i] - x)
        return cnt

# 462. Minimum Moves to Equal Array Elements II
