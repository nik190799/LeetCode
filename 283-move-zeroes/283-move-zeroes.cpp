class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int zero_count = 0, v_size = nums.size();
        for(int i=0;i<v_size;i++){
            if(nums[i]==0){
                nums.erase(nums.begin() + i);
                zero_count++;
                i--;
                v_size--;
            }
        }
        for(int i=0;i<zero_count;i++){
            nums.push_back(0);
        }
    }
};