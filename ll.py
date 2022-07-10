#create a class to rep your linkedlist

# class LinkedList:
#     def __init__(self):
#         self.head = None  #where the list starts is the head of the list

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return  "-->".join(nodes)

    def __iter__(self):  #to have same behavior as normal list, always validate that current node is not none
        node = self.head  #wen condition is true you have reached the end of your linkedlist
        while node is not None:
            yield node   #goes tru the list and yields every single node
            node = node.next   #move to next node

    def add_first(self, node):
        node.next = self.head  #s.h as the next reference of the new node so dat the new node pts to the old self
        self.head = node  #new head of the list is the inserted node

    def add_last(self, node):
        if self.head is None:   #transverse the whole list until you reach the end
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node  #set current node as last node, add new node as next value

    def add_after(self, target_node_data, new_node):  #inserting after an existing node
        if self.head is None:
            raise Exception('List is empty.')

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with data '%s' not found" % target_node_data)

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception('List is empty.')  #raise an exception if linkedlist is empty or node not present
        if self.head.data == target_node_data:
            return self.add_first(new_node)   #trying to add a new node before the head  of the list

        prev_node = self.head  #to keep track of last checked node using the prev node variable
        for node in self:
            if node.data == target_node_data:   #find the target node
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node
        raise Exception("Node with data '%s' not found" % target_node_data)

    def remove_node(self, target_node_data):
        if self.head is None:    #check that list is not empty
            raise Exception('List is empty')

        if self.head.data == target_node_data:   #check if node to be removed is current head of list, #if it is then u want the next node in the list to bcum the new head
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:   #if none of this happens then u transverse the list looking 4 d node 2 to be removed
            if node.data == target_node_data:
                previous_node.next = node.next   #if u find it update the prev node to pt to its next node automatically removing d found node from the list
                return
            previous_node = previous_node
        raise Exception("Node with dta '%s' not found" % target_node_data)   #after trsnsversing  the whole list and its not found u raise an exception



#to rep each node of the linkedlist


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


# llist = LinkedList()
# first_node = Node('a')
# llist.head = first_node
# print(llist)
#
# second_node = Node('b')
# third_node = Node('c')
# first_node.next = second_node
# second_node.next = third_node
# print(llist)

# llist = LinkedList(['a', 'b', 'c', 'd', 'e'])
# print(llist)

# for node in llist:
#     print(node)

# llist = LinkedList()
# llist.add_first(Node('b'))
# print(llist)
# llist.add_first(Node('a'))
# print(llist)

# llist.add_last(Node('f'))
# llist.add_last(Node('g'))
# print(llist)

# llist = LinkedList(['a', 'b', 'c', 'd'])
# print(llist)
#
# llist.add_after('c', Node('cc'))
# print(llist)
# llist.add_after('f', Node('g'))

# llist = LinkedList()
# llist.add_before('b', Node('a'))
# print(llist)

# llist = LinkedList(['b', 'c'])
# llist.add_before('b', Node('a'))
# llist.add_before('b', Node('cc'))
# print(llist)
# llist.add_before('n', Node('m'))
# print(llist)

# llist.remove_node('a')
llist = LinkedList(['a', 'b', 'c', 'd', 'e'])
print(llist)
llist.remove_node('m')
print(llist)

