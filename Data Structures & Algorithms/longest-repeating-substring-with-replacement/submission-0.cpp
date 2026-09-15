class Solution {
public:
    int characterReplacement(string s, int k) {
        int hash_table['z' -'a' + 1] = {0};
        int max_len = 0;
        int left = 0;
        int right = 0;
        int n = s.size();

        while(right < n){
            hash_table[s[right] - 'A']++;
            while((right - left + 1) - get_most_freq(hash_table) > k ){
                hash_table[s[left] - 'A']--;
                left++;
            }
            max_len = max(max_len, right - left + 1);
            right++;
        }
        return max_len;
    }
    int get_most_freq(int hash_table[]){
        int n = 'z' - 'a' + 1;
        int most_freq = 0;
        for(int i  = 0; i < n;i++){
            if(most_freq < hash_table[i]){
                most_freq = hash_table[i];
            }
        }
        return most_freq;
    }
};
