# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        return self.check(root) != -1
    
    def check(self, root):
        if not root:
            return 0

        left = self.check(root.left)
        right = self.check(root.right)

        # 높이 차이가 나는 경우 -1, 이외에는 높이에 따라 1 증가
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1 # 트리가 위로 올라갈때마다 1씩 
        
        
        
