# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        # Creating a queue to store value
        q = deque()

        # atrting queue from root
        q.append(root)

        # array to store left side view of tree
        node = []

        # Runnning until queue is not empty
        while q:

            # Getting the lengt hof queue
            length = len(q)

            # Appedning the most left element of the current level
            node.append(q[0].val)
            
            # Applying loop on the vhildern of current node
            for i in range(length):
                curr = q.popleft()

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        
        # return  most left value of array
        return node[-1]
            
