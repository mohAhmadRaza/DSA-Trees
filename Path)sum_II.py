# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []

        def DFS(node, currentSum, string):
            if not node:
                return
            
            currentSum += node.val
            string += str(node.val) + " "

            if not node.left and not node.right:
                if currentSum == targetSum:
                    paths.append(list(map(int, string.split())))
                return
            
            DFS(node.left, currentSum, string)
            DFS(node.right, currentSum, string)
        
        DFS(root, 0, "")
        return paths
