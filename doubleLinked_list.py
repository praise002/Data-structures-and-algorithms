class Node:

    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):
        #This method prints list in forward direction. Use node.next
        if self.head is None:
            print('Linked list is empty')
            return

        itr = self.head
        llstr = ''  #linkedlist string
        while itr:
            llstr += str(itr.data) + '--->'
            itr = itr.next
        print(llstr)

    def print_backward(self):
        #print linkedlist in reverse direction.Use node.prev for this.
        if self.head is None:
            print('Linked list is empty')
            return

        last_node =self.get_last_node()
        itr = last_node
        llstr = ''
        while itr:
            llstr += itr.data + '--->'
            itr = itr.prev
        print('Linked list in reverse: ', llstr)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr


if __name__ == '__main__':
    ll = DoublyLinkedList()
