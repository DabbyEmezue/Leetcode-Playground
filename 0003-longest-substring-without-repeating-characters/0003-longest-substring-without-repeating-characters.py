class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        storage = set()
        L = 0
        if len(s) <= 1:
            return len(s)  # Return the length of the string if it's 1 character or 
        for R in range(len(s)):
            while s[R] in storage:
                storage.remove(s[L])
                L += 1
            storage.add(s[R])
            maxLength = max(maxLength, R - L + 1)

        return maxLength
