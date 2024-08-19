# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        # Creating a queue to store value
        q = deque([root])

        # array to store left side view of tree
        node = []

        # Runnning until queue is not empty
        while q:
            # Getting the lengt hof queue
            length = len(q)
            level_max = float('-inf')
            
            # Applying loop on the vhildern of current node
            for i in range(length):
                curr = q.popleft()
                level_max = max(level_max, curr.val)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            node.append(level_max)

        # return  most left value of array
        return node
            
