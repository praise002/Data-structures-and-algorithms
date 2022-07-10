"""
Create a node class
create a linked list
traverse the linked list
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None  #ref to next node


class LinkedList:
    def __init__(self):
        self.head = None   #ll is empty

    def print_ll(self):
        if self.head is None:
            print("Linked list is empty.")
        else:
            n = self.head
            while n is not None:
                print(n.data, "--->", end=" ")  #the data of the first node
                n = n.ref

    def add_at_beginning(self, data):
        new_node = Node(data)   #create new node, initially pointing to none
        new_node.ref = self.head   #the new node ref should point to the head
        self.head = new_node  #new node is now the head

    def add_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node   #if it is empty take self.head as new_node
        else:
            #go to the last node
            n = self.head
            while n.ref is not None:   #the ref of n is not empty
                n = n.ref   #go to the last node
            n.ref = new_node  #after iterating to n-->null, take the n.ref to point to the new node

    def add_after(self, data, x):   #x is the after node
        n = self.head
        while n is not None:   #if n is first node
            if x == n.data:  #if true we found the x node
                break
            else:  #go to the next node
                n = n.ref   #check until it reach the x node
        #we exit while loop on 2 condition: wen we find the x value or n is none
        if n is None:
            print("Node is not present in ll")
        else:
            new_node = Node(data)  #create new node
            #change the ref, initially pointing to none
            new_node.ref = n.ref  #change new node ref
            n.ref = new_node  #n.ref shud point to new node

    def add_before(self, data, x):
        if self.head is None:
            print("ll is empty!")
            return   #come out of it and not execute any other statement
        if self.head.data == x:  #copy and paste from add_at_beginning, if not none this is executed
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:  #find the prev node of x
            if n.ref.data == x:
                break
            n = n.ref  #otherwise keep executing until x is found

        if n.ref is None:
            print("Node is not found!")  #if prev node is not found
        else:
            new_node = Node(data)  # create new node
            new_node.ref = n.ref  # change new node ref
            n.ref = new_node

    def insert_empty(self, data):
        if self.head is None:  #ll is empty
            new_node = Node(data)   #create new node
            self.head = new_node    #store head in new node
        else:  #if ll not empty
            print("LL is not empty.")

    def delete_at_beginning(self):
        if self.head is None:   #check if head is none
            print("LL is empty so i can't delete nodes!")
        else:  # use return or use else
            self.head = self.head.ref   #point head to second node

    def delete_at_end(self):
        if self.head is None:
            print("LL is empty so i can't delete nodes!")
        elif self.head.ref is None:  #only contains one node
            self.head = None  #so since self.head is none, ll is empty
        else:
            n = self.head
            while n.ref.ref is not None:  #when not none, increment it by n.ref
                n = n.ref
            #assign n.ref to none
            n.ref = None   #when n.ref.ref is none assign n.ref to none to delete the last node

    def delete_by_value(self, x):   #the x is user input
        if self.head is None:  #check if ll is empty
            print("Can't delete, ll is empty.")
            return  #to break out
        #check if first node is given node, pt head to 2nd node using ref
        if x == self.head.data:
            self.head = self.head.ref
            return #so as not to use else
        n = self.head
        while n.ref is not None:  #bcus first node is not none
            if x == n.ref.data:  #when we get the prev node
                break
            n = n.ref  #increment it if not x
        if n.ref is None:
            print("Node is not present!")
        else:   #found the prev node
            #change the ref to another node since we have to delete x
            n.ref = n.ref.ref


ll = LinkedList()
# ll.print_ll()
ll.add_at_beginning(10)
ll.add_at_beginning(20)
ll.add_at_beginning(30)
# ll.add_at_end(100)
# ll.add_at_end(500)
# ll.add_at_end(100)
# ll.add_after(200, 100)
# ll.add_before(20, 10)
# ll.add_before(30, 10)
# ll.add_before(30, 60)
# ll.insert_empty(10)
# ll.insert_empty(20)
# ll.delete_at_beginning()
# ll.delete_at_end()
ll.delete_by_value(10)
ll.print_ll()