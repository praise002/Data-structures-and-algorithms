class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None  #empty linkedlist, the starting pt of ll

    def print_ll(self):
        if self.head is None:
            print('Linked list is empty.')
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.next  #to go to the next value

    def add_at_beginning(self, data):
        new_node = Node(data)  #create a new node, its pointing to none so we need to change it
        new_node.next = self.head  #change new node ref to head, initially it was none
        self.head = new_node   #store new node as first node which is head



ll = LinkedList()
ll.print_ll()
ll.add_at_beginning(10)
ll.print_ll()



node = Node(10)   #gives the ref
print(node)