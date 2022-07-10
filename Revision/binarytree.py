class BST:
    def __init__(self, key):
        self.key = key
        self.l_child = None
        self.r_child = None

    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            print("Can't insert duplicate value")
            return
        if self.key > data:
            if self.l_child:  #if present
                self.l_child.insert(data)
            else:
                self.l_child = BST(data)
        if self.key < data:
            if self.r_child:
                self.r_child.insert(data)
            else:
                self.r_child = BST(data)

    def search(self, data):
        if self.key == data:
            print("Node is found")
            return
        if data < self.key:
            if self.l_child:
                self.l_child.search(data)
            else:
                print(data, "is not present in tree")

        if data > self.key:
            if self.r_child:
                self.r_child.search(data)
            else:
                print(data, "is not present in tree")

    def preorder(self):
        print(self.key, end=" ")  #print root node
        if self.l_child:
            self.l_child.preorder()
        if self.r_child:
            self.r_child.preorder()

    def inorder(self):   #results are in ascending order
        if self.l_child:
            self.l_child.inorder()
        print(self.key, end=" ")
        if self.r_child:
            self.r_child.inorder()

    def postorder(self):
        if self.l_child:
            self.l_child.postorder()
        if self.r_child:
            self.r_child.postorder()
        print(self.key, end=" ")

    def levelorder(self):
        q = list()  #an empty queue
        q.append(self.key)  #add root node
        while len(q) != 0:  #stopping condition wen it bcums 0
            root = q.pop(0)
            print(root)
            if root.l_child is not None:
                q.append(root.l_child)
            if root.r_child is not None:
                q.append(root.r_child)   #work on it

    def delete(self, data, curr):
        if self.key is None:
            print("Tree is empty so can't delete nodes")
            return
        #find d node
        if data < self.key:
            if self.l_child:  #if it is present
                self.l_child = self.l_child.delete(data, curr)
            else:
                print(data, "is not present in the tree")

        elif data > self.key:
            if self.r_child:
                self.l_child = self.l_child.delete(data, curr)
            else:
                print(data, "is not present in the tree")

        else:  #that means it is root node, now other operations will be pting to self
            #check its number of child node, 0child, 1child, 2childs
            if self.l_child is None:  #leaf node
                temp = self.r_child
                if data == curr:  #deleting root node with 1child
                    self.key = temp.key
                    self.l_child = temp.l_child
                    self.r_child = temp.r_child
                    temp = None
                    return
                self = None  #make d lchild none
                return temp  #works for leaf node & 1child
            if self.r_child is None:
                temp = self.l_child
                if data == curr:  #deleting root node with 1child
                    self.key = temp.key
                    self.l_child = temp.l_child
                    self.r_child = temp.r_child
                    temp = None
                    return
                self = None
                return temp
            node = self.r_child
            while node.l_child:  #while lchild is present
                node = node.l_child  #keep searching 4 lchild until it bcums none
            self.key = node.key   #key becomes d smallest value in d tree
            self.r_child = self.r_child.delete(node.key, curr)
        return self

    def min_node(self):
        current = self
        while current.l_child:  #stopping condition, keep executing as long as there is lchild
            current = current.l_child
        print("Node with samllest key is", current.key)

    def max_node(self):
        current = self
        while current.r_child:
            current = current.r_child
        print("Node with biggest key is", current.key)


def count(node):
    if node is None:
        return 0
    return 1 + count(node.l_child) + count(node.r_child)  #1 is root node, it is recursive


root = BST(10)
# root.insert(1)
# root.insert(2)
num = [6, 3, 1, 98, 7]
for i in num:
    root.insert(i)
# print(count(root))
print("Preorder")
root.preorder()
print()
print("Inorder")
root.inorder()
print()
print("Postorder")
root.postorder()
print()
# if count(root) > 1:
#     print("After deleting")
#     root.delete(10, root.key)
# else:
#     print("Can't perform deletion operation!")
root.preorder()
print("Levelorder")
root.levelorder(root)
# root.search(100)
print()
# root.min_node()
# root.max_node()