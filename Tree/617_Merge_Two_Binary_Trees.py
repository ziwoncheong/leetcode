# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        
        root_node = None
        
        if not t1:
			# t1 is empty, new tree is decided by t2
            return t2
        
        elif not t2:
			# t2 is empty, new tree is decided by t1
            return t1
        
        else:
            # both t1 and t2 exist, merge current node, and traverse on DFS again
            root_node =  TreeNode( t1.val + t2.val )
            root_node.left = self.mergeTrees( t1.left, t2.left )
            root_node.right = self.mergeTrees( t1.right, t2.right )
            
            return root_node
        
