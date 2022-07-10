import collections


queue = collections.deque()
print(queue)
queue.append(50)
queue.append(40)
queue.append(30)
queue.append(20)
print(queue)
print(len(queue) == 0)
print(len(queue))
print(queue[-1])

queue.popleft()
queue.popleft()
queue.popleft()
queue.popleft()
print(queue)


"""Part 2"""
print()
queue = collections.deque()
queue.appendleft(10)
queue.appendleft(20)
queue.appendleft(30)
queue.appendleft(60)
print(queue)
print(queue[0])

queue.pop()
queue.pop()
print(queue)


"""Part 3"""
print()
queue = list()


def enqueue():
    element = input("Enter the element: ")
    queue.append(element)
    print(element, "is added to queue")


def dequeue():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        q = queue.pop(0)
        print(q, "is removed from the list")


def peek():
    if not queue:
        print("queue is empty")
    else:
        e = queue[-1]
        print(e, "is the last element in the queue")


def length():
    print(len(queue))


def display():
    print(queue)


while True:
    print("Select the operation 1. enqueue 2. dequeue 3. peek 4. length 5. display 6. quit")
    choice = int(input())
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        peek()
    elif choice == 4:
        length()
    elif choice == 5:
        display()
    elif choice == 6:
        break
    else:
        print("Incorrect operation")




