class Solution:
    def isValid(self, s: str) -> bool:
            
        def isOpen(s):
            return s in ["(", "[", "{"]
        
    
        def isPair(s1, s2):
            return s1+s2 in ["()", "[]", "{}"]
        
        b = [] # brackets
        for i in range(len(s)):
            if isOpen(s[i]):
                b.append(s[i])
            else:
                if not b: return False
                if not isPair(b.pop(), s[i]):return False
        
        return not b
        