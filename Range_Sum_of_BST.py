# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = []

        def InOrder(curr, arr):
            if not curr:
                return None
            
            InOrder(curr.left, arr)
            arr.append(curr.val)
            InOrder(curr.right, arr)
        
        InOrder(root, result)

        lowIndex, highIndex = result.index(low), result.index(high)
        return sum(result[lowIndex:highIndex+1])
        
