class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        result = 0
        maxf = 0
        L = 0
        
        for R in range(len(s)):
            count[s[R]] = count.get(s[R], 0) + 1
            maxf = max(maxf, count[s[R]])
            
            # Check if we need more replacements than k
            if (R - L + 1) - maxf > k:
                count[s[L]] -= 1
                L += 1
            
            result = max(result, R - L + 1)
           
        return result
