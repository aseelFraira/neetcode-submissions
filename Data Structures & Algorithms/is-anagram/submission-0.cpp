class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()) return false;
        int n = s.size();
        int size = 'z' - 'a' + 1;
        int hist1[size] = {0};
        int hist2[size] = {0};

        for(int i = 0; i < n; i++){
            hist1[s[i] - 'a']++;
            hist2[t[i] - 'a']++;
        }

        return comapreHists(hist1,hist2); 
    }
    bool comapreHists(int hist1[],int hist2[]){
        int size = 'z' - 'a' + 1;
        for(int i = 0;i < size; i++){
            if(hist1[i] != hist2[i]) return false;
        }
        return true;
    }
};
