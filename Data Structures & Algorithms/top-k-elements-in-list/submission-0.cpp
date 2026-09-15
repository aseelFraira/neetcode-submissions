class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> map;
        int n = nums.size();
       vector<vector<int>> buckets(n + 1);
       vector<int> res;

       for(int num : nums){
        map[num]++;
       }
       for(auto p : map){
        buckets[p.second].push_back(p.first);
       }
       for(int i = n; i >= 0 && res.size() < k; i--){
            for (int num : buckets[i]) {
                res.push_back(num);   
            if (res.size() == k) break;
            }
       }
       return res;
       
    }
    
};
