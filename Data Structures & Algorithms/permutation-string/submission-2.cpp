class Solution {
public:
        bool checkInclusion(string s1, string s2) {
            int n = s2.size();
            int offset = s1.size();
            if(offset > n) return false;

            int hist_size = 'z' - 'a' + 1;
            int hist1[hist_size] = {0};
            int hist2[hist_size] = {0};
            for(int i = 0; i < offset;i++){
                hist2[s2[i] - 'a']++;
                hist1[s1[i] - 'a']++;
            }


            int left = 0;
            int right = offset;

            while(right < n){
                if(compare_hists(hist1,hist2)){
                    return true;
                }
                hist2[s2[left] - 'a']--;
                hist2[s2[right] - 'a']++;
                left++;
                right++;

            }
            return compare_hists(hist1,hist2);
        }
        bool compare_hists(int hist1[],int hist2[]){
            int N = 'z' - 'a' + 1;
            for(int i  = 0; i < N; i++){
                if(hist1[i] != hist2[i]) return false;
            }
            return true;
        }
};
