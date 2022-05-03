class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        m = {}
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff not in m:
                m[numbers[i]] = i
            else:
                return [m[diff]+1,i+1]

        
                
            
            
                