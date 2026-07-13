# 1291. Sequential Digits

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res=[]
        start=1
        while start<10:
            temp=start
            while temp<=high:
                curr_temp=temp%10
                temp*=10
                if curr_temp<9:
                    temp+=(curr_temp+1)
                else:
                    break
                if temp>=low and temp<=high:
                    res.append(temp)
            start+=1
        
        res.sort()
        return res
        