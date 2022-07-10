class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None  #next ref
        self.pref = None  #prev ref


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):   #forward traversal
        if self.head is None:
            print("ll is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "--->", end=" ")  #data for first node
                n = n.nref   #move to next node

    def traverse_reverse(self):  #backward traversal
        if self.head is None:
            print("ll is empty")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref  #traverse to last node

            while n is not None:  #after reaching last node
                print(n.data, "--->", end=" ")
                n = n.pref  #go to prev node, keep traversing

    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Double ll is not empty!")

    def insert_at_begin(self, data):
        new_node = Node(data)
        if self.head is None:  #if ll is empty create new node
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node   #make self.head d new node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:  #if empty
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref  # traverse to last node
            n.nref = new_node
            new_node.pref = n

    def add_after(self, data, x):
        if self.head is None:
            print("Double ll is empty so can't insert")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref  #keep iterating
            if n is None:  #after iterating and it is not found
                print("Couldn't find given node in double ll")
            else:  #found x
                new_node = Node(data)
                new_node.pref = n
                new_node.nref = n.nref
                if n.nref is not None:
                    n.nref.pref = new_node  #not necessary
                n.nref = new_node

    def add_before(self, data, x):
        if self.head is None:
            print("Double ll is empty so can't insert")
        else:  #ll is not empty
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:  #after traversing and couldn't find it
                print("Given node not present in double ll")
            else:  #x is found, rest node
                new_node = Node(data)  #general
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:  #when prev node is not none
                    n.pref.nref = new_node
                else:  #if n.pref is none, that means we ar adding before first node
                    self.head = new_node  #pt to new_node
                n.pref = new_node  #if n.pref is none, maybe add before head

    def delete_begin(self):
        if self.head is None:
            print("Double ll is empty so can't delete node")
            return
        if self.head.nref is None:  #only 1 node
            self.head = None
            print("Dll is empty after deleting the node")
        else:
            self.head = self.head.nref
            self.head.pref = None

    def delete_at_end(self):
        if self.head is None:
            print("Dll is empty")
            return
        if self.head.nref is None:   #only 1 node
            self.head = None
            print("Dll is empty after deleting node")
        else:
            n = self.head
            # while n.nref.nref is not None:  #go to prev node
            #     n = n.nref
            # n.nref = None
            while n.nref is not None:  #method 2
                n = n.nref
            n.pref.nref = None

    def delete_by_value(self, x):
        if self.head is None:
            print("Dll is empty so can't delete nodes")
            return
        if self.head.nref is None:  #delete 1 node
            if x == self.head.data:
                self.head = None
                print("Dll is empty after deleting node")
            else:
                print(x, "is not present in dll")  #if its not present
            return
        if x == self.head.data:   #first node
            self.head = self.head.nref  #point head to 2nd node
            self.head.pref = None
            return
        n = self.head
        while n.nref is not None:
            if x == n.data:
                break
            n = n.nref
        if n.nref is not None:
            n.nref.pref = n.nref
            n.pref.nref = n.nref
        else:   #pointing to last node
            if x == n.data:
                n.pref.nref = None
            else:  #if not found
                print(x, "is not found in node")


dll = DoubleLinkedList()
dll.insert_empty(30)
dll.insert_at_begin(40)
dll.insert_at_end(50)
dll.insert_at_end(70)
# dll.add_after(90, 30)
# dll.add_after(100, 70)
# dll.add_after(20, 40)
# dll.add_before(90, 40)
# dll.delete_begin()
# dll.delete_at_end()
# dll.delete_by_value(70)
dll.traverse()