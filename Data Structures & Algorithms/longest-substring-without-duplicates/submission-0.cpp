class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int left = 0;
        int right = 0;
        int max_len = 0;
        unordered_map<int,int> map;

        while(s[right]){
            map[s[right]]++;
            while(map[s[right]] > 1){
                map[s[left++]]--;
            }
            max_len = max(max_len,right - left + 1);
            right++;
        }
        return max_len;
    }
};
