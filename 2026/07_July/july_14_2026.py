# 3336. Find the Number of Subsequences With Equal GCD

MOD, LIM = 1000000007, 201

mu = [0] * LIM
lcms = [[0] * LIM for _ in range(LIM)]
pow2 = [0] * LIM
pow3 = [0] * LIM

for i in range(1, LIM):
    for j in range(1, LIM):
        lcms[i][j] = lcm(i, j)

pow2[0] = 1
pow3[0] = 1

for i in range(1, LIM):
    pow2[i] = (pow2[i - 1] * 2) % MOD
    pow3[i] = (pow3[i - 1] * 3) % MOD

mu[1] = 1
for i in range(1, LIM):
    for j in range(i * 2, LIM, i):
        mu[j] -= mu[i]


class Solution:
    def subsequencePairCount(self, nums: list[int]) -> int:
        mx = max(nums)

        count = [0] * (mx + 1)

        for n in nums:
            count[n] += 1

        for i in range(1, mx + 1):
            for j in range(i * 2, mx + 1, i):
                count[i] += count[j]

        dp = [[0] * (mx + 1) for _ in range(mx + 1)]

        for i in range(1, mx + 1):
            for j in range(1, mx + 1):
                l = lcms[i][j]
                c = 0
                
                if l <= mx:
                    c = count[l]

                ci = count[i]
                cj = count[j]
                dp[i][j] = (pow3[c] * pow2[ci + cj - c * 2] - pow2[ci] - pow2[cj] + 1) % MOD

        res = 0

        for i in range(1, mx + 1):
            for j in range(1, mx // i + 1):
                for k in range(1, mx // i + 1):
                    res += mu[j] * mu[k] * dp[j * i][k * i]

        return (res % MOD + MOD) % MOD









from functools import cache
import math

class Solution:
    def subsequencePairCount(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        
        @cache
        def dp(i: int, gcd1: int, gcd2: int) -> int:
           
            if i == len(nums):
                return 1 if (gcd1 > 0 and gcd1 == gcd2) else 0

            res = dp(i + 1, gcd1, gcd2)

            res = (res + dp(i + 1, math.gcd(gcd1, nums[i]), gcd2)) % MOD

            res = (res + dp(i + 1, gcd1, math.gcd(gcd2, nums[i]))) % MOD
            
            return res
            
        return dp(0, 0, 0)