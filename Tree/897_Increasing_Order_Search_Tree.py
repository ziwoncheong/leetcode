# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        prev_node = None
        
        def helper( node: TreeNode):
                           
            if node.right:
                helper( node.right )

            # prev_novde always points to next larger element for current node
            nonlocal prev_node

            # update right link points to next larger element
            node.right = prev_node

            # break the left link of next larger element
            if prev_node:
                prev_node.left = None

            # update previous node as current node
            prev_node = node

            if node.left:
                helper( node.left)
                
        # ---------------------------------------
        helper( root )
        
        return prev_node
