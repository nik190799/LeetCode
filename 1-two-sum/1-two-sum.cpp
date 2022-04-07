class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ans={0,1};
        unordered_map<int, int> m; 
        for(int i=0;i<nums.size();i++){
            m[nums[i]] = i;
        }
        for(int i=0;i<nums.size();i++){
            int sub = target - nums[i];
            if(m.find(sub) != m.end() && m[sub] != i){
                ans[1] = i;
                ans[0] = m[sub];
            }
        }
        
        return ans;
    }
};