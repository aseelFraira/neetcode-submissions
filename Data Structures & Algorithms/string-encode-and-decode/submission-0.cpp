class Solution {
public:

    string encode(vector<string>& strs) {
        int n = strs.size();
        string res = "";
        for(int i = 0;i < n;i++){
            res += std::to_string(strs[i].size()) + "*"; //change from intger to string
            res += strs[i];
        }
        return res;
    }

    vector<string> decode(string s) {
        vector<string> res;
        int n = s.size();
        for(int i = 0;i < n;){
            size_t pos = s.find("*",i); //read till first *
            int len = stoi(s.substr(i, i - pos));
            res.push_back(s.substr(pos + 1,len));
            i = pos + len + 1;
        }
        return res;
    }
};
