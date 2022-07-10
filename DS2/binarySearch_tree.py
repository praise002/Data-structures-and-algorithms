class BST:
    def __init__(self, key):  #doesnt return anything, a constructor
        self.key = key  #root key
        self.l_child = None
        self.r_child = None  #the 3 is used to create a node

    def insert(self, data):
        if self.key is None:  #node is empty
            self.key = data  #insert a root node data
            return   #exit the fn if true
        if self.key == data:  #ignore duplicate va;ue
            return
        if self.key > data:  #key is root node
            if self.l_child:  #if present
                self.l_child.insert(data)
            else:  #if lchild is not present
                self.l_child = BST(data)  #create a new object using bst class
        else:
            if self.r_child:  #if present
                self.r_child.insert(data)  #perform it recursively
            else:  #if rchild is not present
                self.r_child = BST(data)

    def search(self, data):
        if self.key == data:
            print("Node is found!")
            return
        if data < self.key:
            if self.l_child:  #present
                self.l_child.search(data)  #call the search method again
            else:
                print("Node is not present in tree!")
        else:  #for rchild
            if self.r_child:
                self.r_child.search(data)  #call it recursively, if it bcums false else is executed
            else:
                print("Node is not present in tree!")

    def preorder_traversal(self):
        # print("Pre-order")
        print(self.key, end=" ")  #print root node
        if self.l_child:  #if present, call it again recursively
            self.l_child.preorder_traversal()
        if self.r_child:  #if present
            self.r_child.preorder_traversal()

    def inorder_traversal(self):
        # print("In-order")
        if self.l_child:  #if present, call it again recursively
            self.l_child.inorder_traversal()
        print(self.key, end=" ")  # print root node
        if self.r_child:  #if present
            self.r_child.inorder_traversal()  #call it recursively

    def postorder_traversal(self):
        if self.l_child:  #if present, call it again recursively
            self.l_child.postorder_traversal()
        if self.r_child:  #if present
            self.r_child.postorder_traversal()  #call it recursively
        print(self.key, end=" ")  # print root node

    def delete(self, data, curr):  #curr is root.key
        if self.key is None:
            print("Tree is empty!")
            return
        if data < self.key:
            if self.l_child:  #to check if it is present
                self.l_child = self.l_child.delete(data, curr)  #call it recursively
            else:  #not present
                print("Given node is not present in the tree!")

        elif data > self.key:
            if self.r_child:  #check if rchild is present
                self.r_child = self.r_child.delete(data, curr)
            else:
                print("Given node is not present in the tree!")

        else:  #then its root node, after fulfilling either conditions above
            if self.l_child is None: #0  & 1child node
                temp = self.r_child  #temp is none, if lchild is none, return rchild
                if data == curr:  #if true we are deleting d root node
                    self.key = temp.key
                    self.l_child = temp.l_child  #replace
                    self.r_child = temp.r_child  #replace
                    temp = None
                    return

                self = None
                return temp
            if self.r_child is None:
                temp = self.l_child  #if rchild is none then return lchild
                if data == curr:  #if true we are deleting d root node
                    self.key = temp.key
                    self.l_child = temp.l_child  #replace
                    self.r_child = temp.r_child  #replace
                    temp = None
                    return

                self = None
                return temp
            node = self.r_child
            while node.l_child:
                node = node.l_child
            self.key = node.key
            self.r_child = self.r_child.delete(node.key, curr)
        return self

    def min_node(self):
        current = self  #pointing to root node
        while current.l_child:  #to check if lchild is present, executes when true
            current = current.l_child
        print("Node with smallest key is", current.key)

    def max_node(self):
        current = self
        while current.r_child:  #we need to execute it again and again until it becomes none
            current = current.r_child
        print("Node with maximum key is", current.key)


def count(node):
    if node is None:
        return 0
    return 1 + count(node.l_child) + count(node.r_child)  #1 is root node count


# root = BST(None)
root = BST(10)
lst1 = [6, 3]
for i in lst1:
    root.insert(i)
# root.search(6)
print("preorder")
root.preorder_traversal()
# print()
# print("Inorder")
# root.inorder_traversal()
# print()
# print("Postorder")
# root.postorder_traversal()
# print()
# root.delete(60)
# print("after deleting:")
# root.preorder_traversal()
print(count(root))
root.min_node()
root.max_node()
if count(root) > 1:
    root.delete(10, root.key)
else:
    print("Can't perform deletion operation!")
root.delete()  #not working
# print(root.key)
# print(root.l_child)
# print(root.r_child)

# root.l_child = BST(5)
# print(root.l_child.key)
# print(root.r_child)