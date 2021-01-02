'''
# solution 1: O(mn)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack): return -1
        for i in range(len(haystack) - len(needle) + 1):
            j = 0
            while j < len(needle):
                if haystack[i+j] == needle[j]:
                    j+=1
                else:
                    break
            
            if j == len(needle): return i
        
        return -1
'''                    


'''
# solution 2: O(mn)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: i+len(needle)] == needle:
                return i
        
        return -1
'''

# solution 3: O(m+n)
# KMP algorithm
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:    
        # kmp builder
        def kmpPreprocess(pattern):
            i = 1
            j = 0
            res = [0] * len(pattern)
            while i < len(pattern):
                if pattern[i] == pattern[j]:
                    res[i] = j + 1
                    i+=1
                    j+=1
                elif j > 0:
                    j = res[j-1]
                else:
                    res[i] = 0
                    i+=1
            
            return res
        
        # main loop
        if len(needle) == 0: return 0
        if len(needle) > len(haystack) or (not haystack) or (not needle): return -1
        
        kmp = kmpPreprocess(needle)
        i = 0
        j = 0
        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                i+=1
                j+=1
            elif j > 0:
                j = kmp[j-1]
            else:
                i+=1
                
        if j == len(needle):return i - j
        return -1