# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def findSecondMinimumValue(self, root: TreeNode) -> int:
		def inorderTraversal(root):
			if not root:
				return []
			else:
				return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)
		r = set(inorderTraversal(root))
		if len(r)>=2:
			return sorted(list(r))[1]
		else:
			return -1
        
