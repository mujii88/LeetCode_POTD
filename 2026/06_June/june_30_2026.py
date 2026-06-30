class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        freq=defaultdict(int)
        count=0
        i=0
        j=0
        while j<len(s):
            
            
            freq[s[j]]+=1
            if freq['a']>=1 and freq['b']>=1 and freq['c']>=1:
                freq[s[i]]-=1
                i+=1
                count+=len(s)-j
                
            while freq['a']>=1 and freq['b']>=1 and freq['c']>=1:
                count+=len(s)-j
                freq[s[i]]-=1
                i+=1
            j+=1
        
        return count 
        