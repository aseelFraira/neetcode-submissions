class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> st;
        int N = tokens.size();

        for(int i  = 0; i < N;i ++){
            string curr_token = tokens[i];
            if(curr_token == "+" || (curr_token == "*") ||
             (curr_token == "-") || (curr_token == "/")){
                int exp2 = st.top();
                st.pop();
                int exp1 = st.top();
                st.pop();
                if(curr_token == "+") st.push(exp1 + exp2);
                if(curr_token == "*") st.push(exp1 * exp2);
                if(curr_token == "-") st.push(exp1 - exp2);
                if(curr_token == "/") st.push(exp1/exp2);
             }else{
                st.push(stoi(curr_token));
             }
        }
        return st.top();
    }
};
