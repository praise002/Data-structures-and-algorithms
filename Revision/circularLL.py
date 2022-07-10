class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.end = None

    def traverse(self):
        if self.head is None:
            print("Circular ll is empty")
        else:
            n = self.head
            while n is not None:  #stopping condition
                print(n.data, "--->", end=" ")
                n = n.nref
                if n == self.head:
                    break

    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            self.end = new_node
        else:
            print("Circular ll is not empty")

    def add_at_begin(self, data):
        if self.head is None:
            self.insert_empty(data)
        else:  #head is not none
            new_node = Node(data)
            new_node.nref = self.head  #point new node to head
            self.head.pref = new_node  #point headpref to newnode
            new_node.pref = self.end  #point newnode prev ref to end
            self.head = new_node  #make newnode the head
            self.end.nref = self.head  #make end point to head

    def add_at_end(self, data):
        if self.head is None:
            self.insert_empty(data)
        else:
            if self.end is not None:
                new_node = Node(data)
                self.end.nref = new_node
                new_node.pref = self.end
                new_node.nref = self.head
                self.head.pref = new_node
                self.end = new_node  #make new node the end

    def add_after(self, data, x):
        if self.head is None:
            print("Circular ll is empty")
        n = self.head
        while n is not self.end:
            if x == n.data:
                break
            n = n.nref #keep traversing
        if x != n.data:
            print(x, "is not present in circular ll")
            return

        if x is self.head:  #only 1 node or last node
            self.add_at_end(data)
        else:   #we found x
            new_node = Node(data)
            new_node.pref = n
            new_node.nref = n.nref
            n.nref.pref = new_node
            n.nref = new_node

    def add_before(self, data, x):
        if self.head is None:
            print("Circular ll is empty")
            return
        if x == self.head.data:  #add before 1st node
            self.add_at_begin(data)
            return
        n = self.head
        while n is not self.end:
            if n.data == x:
                break
            n = n.nref
        if n.data != x:
            print(x, "is not found")
        else:  #x is found
            new_node = Node(data)
            new_node.nref = n
            new_node.pref = n.pref
            n.pref.nref = new_node
            n.pref = new_node

    def delete_at_begin(self):
        if self.head is None:
            print("Circular ll is empty so can't delete nodes")
            return
        if self.head == self.end:  #only 1 node
            self.head = self.end = None
            print("Circular ll is empty after deleting node")
            return
        else:  #rest node
            self.head = self.head.nref   #make the next node d head
            self.head.pref = self.end   #point head to end
            self.end.nref = self.head  #point end to head

    def delete_at_end(self):
        if self.head is None:
            print("Circular ll is empty so can't delete nodes")
            return
        if self.head == self.end:  #only 1 node
            self.head = self.end = None
            print("Circular ll is empty after deleting node")
            return
        if self.end:
            last_node = self.end
            prev_to_last_node = self.end.pref
            self.end = None  #d last node is deleted
            self.end = prev_to_last_node  #make d prev to last node the new ene
            self.end.nref = self.head  #point its next ref to head
            self.head.pref = self.end  #point its prev ref to new end

    def delete_by_value(self, x):
        if self.head is None:
            print("Circular ll is empty so can't delete nodes")
            return
        if x == self.head.data:
            self.delete_at_begin()
            return
        if x == self.end:
            self.delete_at_end()
            return
        n = self.head
        while n.nref is not self.end:
            if x == n.nref.data:
                break
            n = n.nref   #if not keep traversing
        if n.nref.data != x:
            print(x, "is not found")
        else:   #node is found
            next_node = n.nref.nref
            n.nref = n.nref.nref  #give it d next node
            next_node.pref = n   #point its pref to d node


cll = CircularLinkedList()
cll.insert_empty(10)
# cll.insert_empty(50)
cll.add_at_begin(20)
cll.add_at_begin(50)
cll.add_at_begin(60)
cll.add_at_end(40)
# cll.add_at_end(50)
# cll.add_after(90, 20)
# cll.add_before(70, 10)
# cll.delete_at_begin()
# cll.delete_at_begin()
# cll.delete_at_end()
# cll.delete_at_end()
cll.delete_by_value(40)
cll.traverse()


