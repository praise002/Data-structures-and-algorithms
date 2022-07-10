class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next  #a pointer to the next element


class LinkedList:
    def __init__(self):
        self.head = None  #points to the head of the linkedlist

    def insert_at_beginning(self, data):
        node = Node(data, self.head)  #a pointer to the next element
        self.head = node

    def print(self):
        if self.head is None:
            print('Linked list is empty.')
            return

        itr = self.head   #iterator
        llstr = ''  #linked list string

        while itr:
            llstr += str(itr.data) + '--->'
            itr = itr.next

        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid index')

        if index == 0:
            self.head = self.head.next  #pointing to the next element
            return

        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception('Invalid Index')

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        #search for first occurence of data after in linkedlist
        if self.head is None:
            return
        #Now insert data_to_insert after data_after node
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break

            itr = itr.next

    def remove_by_value(self, data):
        #remove first node that contains data
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next


if __name__ == '__main__':
    ll = LinkedList()
    # ll.insert_at_beginning(5)
    # ll.insert_at_beginning(89)
    # ll.insert_at_end(79)
    # ll.insert_at_end(3)
    ll.insert_values(['banana', 'mango', 'grapes', 'orange'])
    ll.print()
    print('Length of linkedlist: ', ll.get_length())
    ll.remove_at(2)
    # ll.remove_at(-3)
    ll.print()
    ll.insert_at(0, 'guava')
    ll.print()
    ll.insert_at(2, 'jackfruit')
    ll.print()
    ll.insert_after_value('mango', 'apple')  #insert apple after mango
    ll.print()
    ll.remove_by_value('banana')
    ll.remove_by_value('mango')
    ll.remove_by_value('apple')
    ll.remove_by_value('grapes')
    ll.print()


