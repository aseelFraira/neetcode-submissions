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
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        //inOrder on the tree and check
        stack<TreeNode*> st1;
        TreeNode* curr1 = root;

        while(!st1.empty() || curr1){
            while(curr1){
                st1.push(curr1);
                curr1 = curr1->left;
            }
            curr1 = st1.top();
            st1.pop();
            if(isSameTree(curr1,subRoot)) return true;
            curr1 = curr1->right;
        }
        return false;
        
    }
    bool isSameTree(TreeNode* a, TreeNode* b){
        if(!a && !b) return true;
        if(!a && b || a && !b) return false;
        bool leftSub = isSameTree(a->left,b->left);
        bool rightSub = isSameTree(a->right,b->right);
        if(a->val != b->val) return false;
        return leftSub && rightSub;
    }
};
