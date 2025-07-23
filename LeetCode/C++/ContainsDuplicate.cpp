class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        std::map<int, int> hmap;
        
        for (int i = 0; i < nums.size(); i++) {
            if (++hmap[nums[i]] > 1) 
                return true;
        }
        return false;
    }
};