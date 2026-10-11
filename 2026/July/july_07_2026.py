# 3754. Concatenate Non-Zero Digits and Multiply by Sum I

class Solution:
    def sumAndMultiply(self, n: int) -> int:
        curr=0
        sum=0
        while n>0:
            temp=n%10
            if temp>0:
                curr=(curr*10)+n%10
                sum+=n%10
            n=n//10
        
        res=0
        while curr>0:
            temp=curr%10
            if temp>0:
                res=(res*10)+curr%10
            curr=curr//10

        return res*sum
        