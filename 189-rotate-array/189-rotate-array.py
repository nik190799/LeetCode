class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k:
            temp = nums.pop()
            nums.insert(0,temp)
            k -= 1
            
        return nums
            