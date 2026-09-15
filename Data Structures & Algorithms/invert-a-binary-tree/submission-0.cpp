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
    TreeNode* invertTree(TreeNode* root) {
        if(!root);
        invertTree_aux(root);
        return root;
    }
    void invertTree_aux(TreeNode* root) {
        if(!root) return;
        invertTree_aux(root->left);
        invertTree_aux(root->right);
        TreeNode* temp = root->left;
        root->left = root->right;
        root->right = temp;
    }
};
