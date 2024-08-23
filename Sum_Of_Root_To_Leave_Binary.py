# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def DFS(node, binary):
            if not node:
                return 0
            
            binary += str(node.val)
            
            if not node.left and not node.right:
                return int(binary, 2)

            LeftSum = DFS(node.left, binary)
            RightSum = DFS(node.right, binary)

            return LeftSum + RightSum
        
        return DFS(root, "")
