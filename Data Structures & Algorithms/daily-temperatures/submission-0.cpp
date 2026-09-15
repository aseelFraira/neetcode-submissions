class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<int> st;
        int N = temperatures.size();
        vector<int> res(N,0);
        for(int i  = 0; i < N; i++){
            if(!st.empty()){ 
                while(!st.empty() && temperatures[i] > temperatures[st.top()]){
                    res[st.top()] = i - st.top();
                    st.pop();
                }
            }
            st.push(i);
        }
        return res;
        
    }
};
