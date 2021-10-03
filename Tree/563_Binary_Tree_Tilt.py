# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        def total_value(root):
            if not root:
                return 0
            return root.val + total_value(root.left) + total_value(root.right)
            
        def diff_value(root):
            if not root:
                return 0
            return abs(total_value(root.left) - total_value(root.right)) + diff_value(root.left) + diff_value(root.right)
        
        
        # recursive
        return diff_value(root)
