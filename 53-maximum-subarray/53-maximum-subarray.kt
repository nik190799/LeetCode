class Solution {
    fun maxSubArray(nums: IntArray): Int {
        var max_sum = nums[0]
        var sum = 0
        for(i in nums){
            sum = sum + i
            if(sum > max_sum) max_sum = sum
            if(sum<0) sum = 0
        }
        return max_sum
    }
}