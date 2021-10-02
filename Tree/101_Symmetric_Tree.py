# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: # root가 없는 경우
            return True
        return self.check(root.left, root.right)
    
    def check(self, left, right):
        if left == None and right == None: # 좌우 둘 다 없으면 True
            return True
        if left == None or right == None: # 좌우 둘 중 하나만 없으면 False
            return False
        if left.val != right.val: # 좌우 값이 다르면 False
            return False
        
        a = self.check(left.left, right.right) # 좌의 좌 값과 우의 우값 비교
        b = self.check(left.right, right.left) # 좌의 우 값과 우의 좌값 비교
        return a and b
        
class Solution2:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = collections.deque([(root.left, root.right)])
        while stack:
            l, r = stack.pop()
            if l is None and r is None:
                continue
            if l is None or r is None:
                return False
            if l.val != r.val:
                return False
            stack.append((l.left, r.right))
            stack.append((l.right, r.left))
        return True
