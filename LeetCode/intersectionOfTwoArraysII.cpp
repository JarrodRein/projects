class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        
        vector <int> vec;
       int count =0;
        for(int i=0; i<nums1.size(); i++){
            for(int j=0; j<nums2.size(); j++){
                if(nums1[i]==nums2[j] && count ==0){
                    count++;
                    vec.push_back(nums1[i]);
                }
                
            }
            count =0;
        }
        return vec;
    }
};