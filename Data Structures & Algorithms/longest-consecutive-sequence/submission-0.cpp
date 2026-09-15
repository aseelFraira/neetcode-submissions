class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
    unordered_map<int,int> mp;  // stores length of sequence at boundaries
    int longest = 0;

    for (int num : nums) {
        if (mp.count(num)) continue; // avoid duplicates

        int left = mp.count(num - 1) ? mp[num - 1] : 0;
        int right = mp.count(num + 1) ? mp[num + 1] : 0;

        int total_len = left + 1 + right;
        mp[num] = total_len;

        // Update boundaries
        mp[num - left] = total_len;
        mp[num + right] = total_len;

        longest = max(longest, total_len);
    }
    return longest;
}

};
