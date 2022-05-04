class Solution:
    def minDeletions(self, s: str) -> int:
        m = {}
        count = 0
        count_set = set()
        for i in s:
            if i not in m:
                m[i] = 1
            else:
                m[i] += 1
        print(m)
        for i in m.values():
            
            if i in count_set:
                for j in range(1,i+1):
                    count += 1
                    if i-j not in count_set:
                        count_set.add(i-j)
                        break
                    
            else:
                count_set.add(i)      
        
        return count
        
        