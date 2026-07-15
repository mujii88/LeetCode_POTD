# 3658 GCD of Odd and Even Sums

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        curr=1
        even=0
        odd=0
        while n>0:
            odd+=curr
            even+=curr+1
            curr+=2
            n-=1
        ans=math.gcd(even,odd)
        return ans