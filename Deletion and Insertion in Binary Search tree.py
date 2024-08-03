class TreeNode:
    def __init__(self, value):
        self.val = value
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def get_successor(self, curr):
        curr = curr.right
        while curr is not None and curr.left is not None:
            curr = curr.left

        return curr

    def delete_node(self, root, value):
        if not root:
            return root

        if root.val < value:
            root.right = self.delete_node(root.right, value)
        elif root.val > value:
            root.left = self.delete_node(root.left, value)

        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            successor = self.get_successor(root)
            root.val = successor.val
            root.right = self.delete_node(root.right, successor.val)

        return root

    def insertion(self, root, node):
        if not root:
            return node

        if node.val < root.val:
            root.left = self.insertion(root.left, node)
        elif node.val > root.val:
            root.right = self.insertion(root.right, node)

        return root







