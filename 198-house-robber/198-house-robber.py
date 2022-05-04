class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 0
        elif length == 1:
            return nums[0]
        elif length == 2:
            return max(nums)
        temp = nums
        temp[0] = nums[0]
        temp[1] = nums[1]
        temp[2] = max(nums[2] + nums[0], nums[1])
        for i in range(3,length):
            temp[i] = nums[i] + max(temp[i - 2],temp[i - 3])
        return max(temp)
        
                    
            
        