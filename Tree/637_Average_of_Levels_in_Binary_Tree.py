# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return None
        
        queue = collections.deque([root])
        out = []
        while queue:
            avg = 0
            n = len(queue)
            for _ in range(len(queue)):
                cnode = queue.popleft()
                avg += cnode.val

                if cnode.left:
                    queue.append(cnode.left)
                if cnode.right:
                    queue.append(cnode.right)

            out.append(avg/n)

        return out

            
