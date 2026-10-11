class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        cum=0
        freq=defaultdict(int)
        freq[0]=1
        valid=0
        res=0
        for i in range(len(nums)):
            if nums[i]==target:
                if freq[cum]>0:
                    valid+=freq[cum]
                cum+=1
            else:
                cum-=1
                valid-=freq[cum]
            freq[cum]+=1
            res+=valid

        return res


        