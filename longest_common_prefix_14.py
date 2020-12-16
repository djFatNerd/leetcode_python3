class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""
        # longest common prefix
        lcp = strs[0]
        i = 0
        for i in range(len(strs)-1):
            while len(lcp) >0:
                if strs[i+1].startswith(lcp):
                    # lcp remains
                    break
                else:
                    # decrement lcp from back until prefix matches
                    lcp = lcp[0:-1]
            
            # no lcp, break early
            if lcp=="": break
        
        return lcp