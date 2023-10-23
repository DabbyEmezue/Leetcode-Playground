class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count ={}
        for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            count[letter]=0
        result = 0
        L = 0
        for R in range(len(s)):
            count[s[R]]+=1
            maxf=max(count.values())
            
            if R-L+1 - maxf > k:
                count[s[L]]-=1
                L+=1
            result = max(result,R-L+1)
           
        return result