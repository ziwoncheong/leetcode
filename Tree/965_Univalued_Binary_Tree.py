# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # Recursion 코드
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if root:
            if root.left:
                if root.val != root.left.val:
                    return False
                
            if root.right:
                if root.val != root.right.val:
                    return False
            
        else:
            return True
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
        
class Solution2: # while loop 코드
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        stack = [root]
        while stack:
            cnode = stack.pop()
            if root.val == cnode.val:
                if cnode.left:
                    stack.append(cnode.left)
                if cnode.right:
                    stack.append(cnode.right)
            else:
                return False
        return True
