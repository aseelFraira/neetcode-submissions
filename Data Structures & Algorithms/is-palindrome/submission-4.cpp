class Solution {
public:
    bool isPalindrome(string s) {
        int n = s.size();
        int left = 0;
        int right = n - 1;

        while(left < right){
            while(left < right && !is_letter_num(s[left])) left++;
            while(right > left && !is_letter_num(s[right])) right--;
            char l = tolower(s[left]);
            char r = tolower(s[right]);
            if(l != r) return false;
            left++;
            right--;
        }
        return true;
    }
    bool is_letter_num(char s){
        return s >= 'a' && s <= 'z' || s >= 'A' && s <= 'Z' || s >= '0' && s <= '9';
    }
};
