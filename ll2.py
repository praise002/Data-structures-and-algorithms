class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next   #a pointer to the next element


class LinkedList:
    def __init__(self):
        self.head = None   #it pts to the end of the ll

    def insert_at_beginning(self, data):
        node = Node(data, self.head)  #the self.head would be the current head
        self.head = node

    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return

        itr = self.head     #if not blank
        llstr = ''    #for each itr we want to create a value
        while itr:
            llstr += str(itr.data) + '--->'
            itr = itr.next

        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        #not blank
        itr = self.head
        while itr.next:
            itr = itr.next
        #at the last element
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None  #inserting a new value
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    #to remove element at a given index
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('This is not a valid index')

        if index == 0:   #trying to remove the head
            self.head = self.head.next  #pointing to the next element
            return

        count = 0
        itr = self.head
        while itr:   #goes tru each element in ll
            if count == index - 1:
                itr.next = itr.next.next  #when we remove that element it pts to next element next
                break

            itr = itr.next
            count += 1

    #insert at index and the value
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception('Invalid index')

        #if valid
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



if __name__ == "__main__":
    ll = LinkedList()
    # ll.insert_at_beginning(5)
    # ll.insert_at_beginning(69)
    # ll.insert_at_end(79)
    # ll.insert_at_end(65)
    ll.insert_values(['banana', 'mango', 'grapes', 'orange'])
    ll.print()
    ll.remove_at(2)
    # ll.remove_at(20)
    ll.insert_at(0, 'figs')
    ll.insert_at(2, 'jackfruit')
    ll.print()
    print("Length:", ll.get_length())