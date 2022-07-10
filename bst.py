class Treenode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def find_min(self, root):
        current = root
        while current.left:  #while left exist
            current = current.left
        return current

    def delete_node(self, root: Treenode, key: int) -> Treenode:
        if not root:  #if root does not exist
            return root

        elif key < root.val:
            root.left = self.delete_node(root.left, key)

        elif key > root.val:
            root.right = self.delete_node(root.right, key)

        else:
            if not root.left and not root.right:  #it has no children, leaf
                root = None  #change its value to none

            #1 child
            elif not root.left:  #root.left does not exist
                root = root.right

            elif not root.right:  #root.right does not exist
                root = root.left

            else:  #2child exist
                temp = self.find_min(root.right)
                root.val = temp.val  #change the value of our root to that value
                root.right = self.delete_node(root.right, temp.val)  #temp.val to remove d min val bcus its now a duplicate
        return root
