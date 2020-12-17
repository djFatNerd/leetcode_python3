class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        l = []
        if not digits: return l
        d = {} 
        d['2'] = 'abc'
        d['3'] = 'def'
        d['4'] = 'ghi'
        d['5'] = 'jkl'
        d['6'] = 'mno'
        d['7'] = 'pqrs'
        d['8'] = 'tuv'
        d['9'] = 'wxyz'
        
        # recursive helper method
        # write inside so we don't need to pass d & l in every recursive call
        def helper(digits, s):
            if len(digits) == 0:
                l.append(s)
            else:
                for c in d[digits[0]]:
                    helper(digits[1:], s+c)      
        
        helper(digits, '')
        return l
    
