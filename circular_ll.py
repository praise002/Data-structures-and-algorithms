class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def transverse(self, starting_point=None):   #define the start and end of iteration
        if starting_point is None:
            starting_point = self.head
        node = starting_point
        while node is not None and (node.next != starting_point):
            yield node
            node = node.next
        yield node

    def print_list(self, starting_point=None):
        nodes = []
        for node in self.transverse(starting_point):
            nodes.append(str(node))
        print('--->'.join(nodes))


circular_llst = CircularLinkedList()
circular_llst.print_list()

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')

a.next = b
b.next = c
c.next = d
d.next = a
circular_llst.head = a
circular_llst.print_list()

circular_llst.print_list(b)

circular_llst.print_list(d)
