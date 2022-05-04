class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 0
        elif length == 1:
            return nums[0]
        elif length == 2:
            return max(nums)
        arr = nums
        arr[0] = nums[0]
        arr[1] = nums[1]
        arr[2] = max(nums[2] + nums[0], nums[1])
        for i in range(3,length):
            arr[i] = nums[i] + max(arr[i - 2],arr[i - 3])
        return max(arr)
        
                    
            
        