class Solution:
    def processStr(self, s: str) -> str:
        curr_s=""
        for i in range(len(s)):
            if s[i] not in {"*","%","#"}:
                curr_s+=s[i]
            elif s[i]=="#":
                temp=curr_s
                curr_s+=temp
            elif s[i]=="%":
                curr_s=curr_s[::-1]
            else:
                curr_s=curr_s[:-1]

        return curr_s        


 # 3612. Process String with Special Operations I