# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.diameterOfBinaryTree_aux(root)[1]
    def diameterOfBinaryTree_aux(self, root: Optional[TreeNode]) ->list: #[max of hiegths, diameter]

        if root is None:
            return [0,0]
        left_height,left_dimeter = self.diameterOfBinaryTree_aux(root.left)
        right_height,right_diameter = self.diameterOfBinaryTree_aux(root.right)

        curr_diameter = left_height + right_height
        max_diameter = max(curr_diameter,left_dimeter,right_diameter)



        return (max(left_height,right_height) + 1,max_diameter)


        

        