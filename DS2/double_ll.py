class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None  #ref to next node
        self.pref = None  #prev ref


class Double_ll:
    def __init__(self):
        self.head = None  #ll is empty

    def print_ll(self):   #forward traversal
        if self.head is None:
            print("Linked list is empty.")
        else:
            n = self.head
            while n is not None:
                print(n.data, "--->", end=" ")  # the data of the first node
                n = n.nref

    def print_ll_reverse(self):   #backward reversal
        print()
        if self.head is None:
            print("Linked list is empty.")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref   #traverse to last node

            while n is not None:  #after reaching last node, make it n & print d data
                print(n.data, "--->", end=" ")
                n = n.pref

    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)  #create new node
            self.head = new_node  #pt head to new node
        else:  #if ll is not empty
            print("LL is not empty.")

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None: #check if ll is empty
            self.head = new_node  #take head as new node
        else:  #ll not empty
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)  #create node
        if self.head is None:  #check if ll is empty
            self.head = new_node  #pt head to new node
        else:  #if not empty
            n = self.head #traverse to last node
            while n.nref is not None:
                n = n.nref  #go to next node
            n.nref = new_node
            new_node.pref = n

    def add_after(self, data, x):
        if self.head is None:
            print("LL is empty, so you can't insert.")
        else:  #if ll is not empty
            n = self.head
            while n is not None:
                if x == n.data:  #check
                    break  #if true, break
                n = n.nref  #if false, execute this, keep iterating
            if n is None:  #cudnt find it
                print("Given node is not present in the DLL.")
            else:  #found x
                new_node = Node(data) #create node
                new_node.nref = n.nref
                new_node.pref = n
                if n.nref is not None:  #check if inserting after last node
                    n.nref.pref = new_node
                n.nref = new_node  #if none

    def add_before(self, data, x):
        if self.head is None:
            print("LL is empty, so you can't insert.")
        else:  #if ll is not empty
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("Given node is not present in the DLL.")
            else:  #insert before x, check if inserting b4 1st node
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                else: #if n.nref is none
                    self.head = new_node  #head shud pt to new node
                n.pref = new_node

    def delete_begin(self):
        if self.head is None:
            print("Dll is empty so can't delete any nodes.")  #check if dll is empty
            return
        if self.head.nref is None:  #if its only 1 node
            self.head = None
            print("Dll is empty after deleting the node.")
        else:
            self.head = self.head.nref  #pt head to 2nd node
            self.head.pref = None  #prev ref of 2nd node needs to pt to None

    def delete_end(self):
        if self.head is None:
            print("Dll is empty so can't delete any nodes.")  #check if dll is empty
            return
        if self.head.nref is None:  #if its only 1 node
            self.head = None
            print("Dll is empty after deleting the node.")
        else:
            n = self.head
            while n.nref is not None:  #go 2 d last node
                n = n.nref  #move to d next node, if not none
            n.pref.nref = None

    def delete_by_value(self, x):  #x is the node we want to delete
        if self.head is None:
            print("Dll is empty so can't delete any nodes.")  #check if dll is empty
            return
        if self.head.nref is None:  #if its only 1 node
            if x == self.head.data:  #check if x is the node, if yes, delete
                self.head = None
            else:
                print("X is not present in DLL.")  #if not
            return
        if self.head.data == x:  #deleting first node, if its 1st node do d below
            self.head = self.head.nref  # pt head to 2nd node
            self.head.pref = None  # prev ref of 2nd node needs to pt to None
            return
        n = self.head
        while n.nref is not None:
            if x == n.data:  #if it is x break
                break
            n = n.nref  #if not move to next node
        if n.nref is not None:
            n.nref.pref = n.pref
            n.pref.nref = n.nref
        else:  #if n.nref is none, dat means its pointing to last node
            if n.data == x:  #if true, del last node
                n.pref.nref = None
            else:  #if x is not found
                print("X is not present in Dll!")


dl = Double_ll()
dl.print_ll()
dl.print_ll_reverse()
dl.insert_empty(10)
dl.insert_at_beginning(20)
dl.insert_at_end(30)
dl.add_after(100, 20)
# dl.add_before(50, 100)
# dl.delete_begin()
# dl.delete_end()
dl.delete_by_value(20)
dl.print_ll()

