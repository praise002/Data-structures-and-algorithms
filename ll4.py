class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head is None:
            print('Linked list is empty.')
            return

        n = self.head  # iterator
        llstr = ''  #an empty string

        while n is not None:   #or while n
            llstr = llstr + str(n.data) + '--->'
            n = n.next
        print(llstr)

    def add_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


ll = LinkedList()
ll.print_ll()
ll.add_at_beginning(10)
ll.add_at_beginning(20)
ll.add_at_beginning(30)
ll.print_ll()


