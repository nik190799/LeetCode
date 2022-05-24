class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s == t:
            return False
        
        if abs(len(s) - len(t)) > 1:
            return False
        
        edit = 0
        i = j = 0
        
        while i < len(s):
            if j < len(t):
                if s[i] != t[j]:
                    edit += 1
                    
                    if edit > 1:
                        return False
                    
                    if len(s) == len(t):
                        i += 1
                        j += 1
                        
                    elif len(s) > len(t):
                        i += 1
                    else:
                        j += 1
                else:
                    i += 1
                    j += 1
                    
            else:
                break
        
        return True if edit < 2 else False