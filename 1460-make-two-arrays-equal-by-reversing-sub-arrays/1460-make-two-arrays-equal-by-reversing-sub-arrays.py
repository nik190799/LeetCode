class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        i = 0
        j = 0
        
        while i < len(target):
            
            if target[i] == arr[j]:
                i += 1
                j += 1
            else:
                while True:
                    j += 1
                    if j < len(target):
                        if target[i] == arr[j]:
                            arr[i:j+1] = arr[i:j+1][::-1]
                            break
                    else:
                        break
                if j >= len(target) and target != arr:
                    return False
                else:
                    j = i+1
                i += 1
        return arr==target
                    
                    
                
