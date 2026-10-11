# 1331. Rank Transform of an Array

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp=list(set(arr))
        temp.sort()
        freq={}
        rank=1
        for i in temp:
            freq[i]=rank
            rank+=1

        ans=[]
        for i in range(len(arr)):
            ans.append(freq[arr[i]])
        return ans

        