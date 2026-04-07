class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_lenght = 0
        l = set()
        j = 0
        for i in range(len(s)):
            while s[i] in l:
                l.remove(s[j])
                j+=1
            lenght = i - j +1
            max_lenght = max(max_lenght,lenght)
            l.add(s[i])

        return max_lenght