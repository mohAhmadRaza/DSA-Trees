# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        

        def DFS(node):
            if not node:
                return
            
            DFS(node.left)
            arr.append(node.val)
            DFS(node.right)

        arr = []
        DFS(root)

        newTree = TreeNode(arr[0])
        i = 1
        def DFSS(node):
            nonlocal i
            if i >= len(arr):
                return
            
            node.right = TreeNode(arr[i])
            i += 1
            DFSS(node.right)

        DFSS(newTree)
        
        return newTree
