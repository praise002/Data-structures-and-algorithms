class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:  #none is d stopping condition
                print(n.data, "--->", end=" ")
                n = n.ref

    def add_at_begin(self, data):
        #create new node
        #point ref of new node to head
        #make the new node head
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_at_end(self, data):
        new_node = Node(data)  #create new node
        if self.head is None:
            self.head = new_node  #make d new node d first node
            return
        n = self.head
        while n.ref is not None:
            n = n.ref  #go to last node
        n.ref = new_node  #wen it is none

    def add_after(self, data, x):
        n = self.head
        while n is not None:  #stopping condition when it becomes none
            if x == n.data:
                break
            n = n.ref  #go to next node
        if n is None:
            print("Node is not present in ll")  #when it becomes none
        else:  #n is not none
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def add_before(self, data, x):
        if self.head is None:
            print("ll is empty")
            return
        if self.head.data == x:  #add at begin
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref

        if n.ref is None:
            print("node is not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("ll is not empty")

    def delete_at_begin(self):
        if self.head is None:
            print("ll is empty so can't delete nodes.")
        else:
            self.head = self.head.ref

    def delete_at_end(self):
        if self.head is None:
            print("ll is empty so can't delete nodes")
        elif self.head.ref is None:  #only one node
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    def delete_by_value(self, x):
        if self.head is None:
            print("ll is empty so can't delete nodes")
            return
        if x == self.head.data:  #check if first node is given node
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if x == n.ref.data:  #to get prev node
                break
            n = n.ref
        if n.ref is None:
            print("node is not present!")
        else:
            n.ref = n.ref.ref


ll = LinkedList()
ll.add_at_begin(10)
ll.add_at_begin(20)
ll.add_at_end(30)
ll.add_at_end(40)
# ll.add_after(60, 40)
# ll.add_before(80, 30)
# ll.insert_empty(400)
# ll.delete_at_begin()
# ll.delete_at_end()
ll.delete_by_value(10)
ll.traverse()


