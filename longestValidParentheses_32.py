# find longest valid substring parentheses in a given string
'''
# 1. brute force
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        # helper method to check if a given string is valid
        def isValid(s):
            stack = []
            for i in range(len(s)):
                if s[i] == "(":
                    stack.append(s[i])
                elif len(stack) > 0 and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            
            return len(stack) == 0
        
        
        # check all even length substrings
        maxlen = 0
        for i in range(len(s)):
            for j in range(i+2, len(s)+1, 2):
                if isValid(s[i:j]): maxlen = max(maxlen, j - i)
        
        return maxlen
'''

'''
# 2. DP
class Solution:
    def longestValidParentheses(self, s:str) ->int:
        # DP[i] represent max len of substring that ends at i 
        maxlen = 0
        dp = [0]*len(s)
        for i in range(len(s)):
            # only when close bracket ")" dp[i] != 0
            if s[i] == ")":
                if i > 0:
                    if s[i-1] == "(":
                        if i > 1: 
                            dp[i] = dp[i-2] + 2
                        else:
                            # first pair
                            dp[i] = 2
                    
                    else: 
                        # ....... ))
                        # dp[i - 1 - dp[i-1] - 1]+(+(...)+)
                        #   i - 1 - dp[i-1] + 1 -1 
                        if (i - 1 - dp[i-1] >= 0) and s[i-1 - dp[i-1]] == "(":
                            dp[i] = dp[i-1] + 2
                            if i - 1 - dp[i-1] - 1>= 0:
                                dp[i] += dp[i - 1 - dp[i-1] - 1]
                
                maxlen = max(maxlen, dp[i])
        
        return maxlen
'''

'''
# 3. Stack, tricky, smart
class Solution:
    def longestValidParentheses(self, s:int) -> int:
        maxlen = 0
        stack = []
        stack.append(-1)
        
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                # think carefully, even in the ")))" case, this will work because the stack remains empty(after .pop())
                stack.pop()
                if len(stack) > 0:
                    maxlen = max(maxlen, i - stack[-1])
                else:
                    stack.append(i)
                    
            
        #if maxlen == 1: return 0
        return maxlen

'''
# 4. 2 counters, O(1) space 
# super smart, super fast
class Solution:
    def longestValidParentheses(self, s:int) ->int:
        # forward+backward pass together scans all possible substrings
        
        # forward pass
        # starting from index i to the end, find the max len valid substring
        maxlen, l, r = 0, 0, 0
        for i in range(len(s)):
            if s[i] == "(": l+=1 
            else:r+=1
            if l==r:maxlen = max(maxlen, 2*l)
            if l<r: l, r = 0, 0
        
        # backward pass
        # starting from index j(end) to the beginning, find the max len valid substring
        l, r = 0, 0
        for j in range(len(s)-1,-1,-1):
            if s[j] == "(":l+=1  
            else:r+=1
            if l==r:maxlen = max(maxlen, 2*l)
            if l>r: l, r = 0, 0
        
        return maxlen