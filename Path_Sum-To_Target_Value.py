from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        paths = []
        def DFS(node, currentSum):
            if not node:
                return False
            
            currentSum += node.val

            if not node.left and not node.right:
                paths.append(currentSum)
                return

            DFS(node.left, currentSum)
            DFS(node.right, currentSum)
        
        DFS(root, 0)
        return paths.count(targetSum) > 0

# Create an example binary tree:
#      5
#     / \
#    4   8
#   /   / \
#  11  13  4
# /  \      \
#7    2      1

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

# Target sum to find in the tree
targetSum = 22

# Create an instance of Solution and run hasPathSum
solution = Solution()
result = solution.hasPathSum(root, targetSum)

# Print the result
print("Has path sum:", result)
