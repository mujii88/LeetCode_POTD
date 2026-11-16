class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            i=0
            new_s=""
            while i<len(s):
                temp=0
                for char in range(i,min(len(s),i+k)):
                    temp+=int(s[char])
                new_s+=str(temp)
                i+=k
            s=new_s
        
        return s



        
# 2243. Calculate Digit Sum of a String
