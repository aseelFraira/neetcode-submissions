/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        stack<TreeNode*> st1;
        stack<TreeNode*> st2;
        TreeNode* curr1 = p;
        TreeNode* curr2 = q;
        if(!curr1 && curr2 || curr1 && !curr2) return false;

        

        while(!st1.empty() || curr1){
            while(curr1 && curr2){
                st1.push(curr1);
                st2.push(curr2);
                if(curr1->val != curr2->val) return false;
                curr1 = curr1->left;
                curr2 = curr2->left;
            }
            if(!curr1 && curr2 || curr1 && !curr2) return false;

            curr1 = st1.top();
            curr2 = st2.top();

            st1.pop();
            st2.pop();

            curr1 = curr1->right;
            curr2 = curr2->right;
            if(!curr1 && curr2 || curr1 && !curr2){
                 return false;
            }
            if(curr1 && curr2 && curr1->val != curr2->val){
                return false;
            }
        }
        return true;
        
    }
};
