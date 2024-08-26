# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        if not root1 and not root2:
            return []
        
        result1 = []
        result2 = []
        
        def DFS(node, array):
            if not node:
                return None
            
            DFS(node.left, array)
            array.append(node.val)
            DFS(node.right, array)

        DFS(root1, result1)
        DFS(root2, result2)
        
        i, j = 0, 0
        finalAnswer = []
        while i < len(result1) and j < len(result2):
            if result1[i] < result2[j]:
                finalAnswer.append(result1[i])
                i += 1
            else:
                finalAnswer.append(result2[j])
                j += 1
        
        if result1[i:]:
            finalAnswer.extend(result1[i:])
        if result2[j:]:
            finalAnswer.extend(result2[j:])
        
        return finalAnswer



        return []
        
