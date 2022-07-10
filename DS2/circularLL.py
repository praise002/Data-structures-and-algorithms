class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.end = None

    def print_ll(self):
        if self.head is None:
            print("Circular linked list is empty.")
        else:
            n = self.head
            while n.ref:
                print(n.data, "--->", end=" ")  #the data of the first node
                n = n.ref
                if n == self.head:
                    break

    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            self.end = new_node
            self.head.ref = new_node
            return
        if self.head is not None:
            print("Circular ll is not empty")

    def add_at_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        n = self.head
        if n is None:
            self.head = new_node
            self.end = new_node
            self.head.ref = self.head
            return
        if self.head is not None:
            self.end.ref = new_node
            new_node.ref = self.head
            self.head = new_node

    def add_at_end(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            self.end = new_node
            self.head.ref = new_node
            return
        if self.end is not None:
            new_node = Node(data)
            self.end.ref = new_node
            self.end = new_node
            new_node.ref = self.head

    def add_after(self, data, x):
        n = self.head
        while n is not self.end:
            if x == n.data:
                break
            n = n.ref

        if x != n.data:
            print("Node is not present in linked list.")
            return

        if x is self.head:
            self.add_at_end(data)
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def add_before(self, data, x):
        n = self.head
        if n is None:
            print("Circular ll is empty!")
            return   #come out of it and not execute any other statement
        if self.head.data == x:  #if 1st node is x
            self.add_at_begin(data)
            return

        while n.ref is not self.end:  #find the prev node of x
            if n.ref.data == x:
                break
            n = n.ref  #otherwise keep executing until x is found

        if n.ref.data != x:
            print("Node is not found!")
        else:  #its = x
            new_node = Node(data)  # create new node
            new_node.ref = n.ref  # change new node ref
            n.ref = new_node

    def delete_at_begin(self):
        if self.head is None:
            print("Circular ll is empty so can't delete node.")
            return
        if self.head != self.end:
            self.head = self.head.ref
            self.end.ref = self.head
        else:  #if head = end, i.e only one node
            self.head = self.end = None

    def delete_at_end(self):
        if self.head is None:
            print("Warning: List is empty.")  #list is already empty
            return
        if self.end.ref == self.end:  #has only one node
            self.head = self.end = None
            return

        #list has more than one node
        #find the 2nd to the last node
        n = self.head
        last_node = self.end
        prev_to_last_node = n.ref.ref
        if prev_to_last_node is not self.end:
            n = n.ref
        n.ref.ref = self.head

    def delete_by_value(self, x):
        if self.head is None:
            print("LL is empty.")
            return
        if x == self.head.data:
            self.delete_at_begin()
            return
        n = self.head
        while n.ref is not self.end:
            if x == n.ref.data:
                break
            n = n.ref  #if not increment it
        if n.ref.data != x:
            print("Node not present.")
        else:  #node found
            n.ref = n.ref.ref


cll = CircularLinkedList()
cll.insert_empty(10)
# cll.insert_empty(20)
cll.add_at_begin(20)
cll.add_at_begin(30)
cll.add_at_end(100)
cll.add_at_end(500)
cll.add_at_begin(90)
cll.add_after(400, 90)
cll.add_before(900, 30)
# cll.delete_at_begin()
# cll.delete_at_begin()
# cll.delete_at_end()
# cll.delete_at_end()
# cll.delete_at_end()
# cll.delete_by_value(20)
cll.delete_by_value(10)
cll.print_ll()

