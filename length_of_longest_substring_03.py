class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        if len(s) == 0: return 0
        
        chars = set()
        max_length = 0
        while i < len(s) and j < len(s):
            if s[j] in chars:
                chars.remove(s[i])
                i+=1
            else:
                chars.add(s[j])
                max_length = max(max_length, j - i + 1)
                j+=1
        
        return max_length


class Solution2:
    def lengthOfLongestSubstring(self, s:str) -> int:
        i = 0
        j = 0
        if len(s) == 0: return 0

        d = {}
        max_length = 0
        while i < len(s) and j < len(s):
            if s[j] in d:
                i = max(d[s[j]] + 1, i)

            max_length = max(max_length, j - i + 1)
            d[s[j]] = j
            j+=1
        
        return max_length
