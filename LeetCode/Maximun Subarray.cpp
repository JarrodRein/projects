class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        auto sum=0, maxs = -1000000;
        for(int i=0; i<nums.size(); i++){
            sum = max(nums[i], nums[i]+sum);
 if(sum>maxs){
            maxs= sum;
        }
        }
       
        return maxs;
    }
};