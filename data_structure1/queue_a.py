"""
It is a linear data structure
enqueue - adding element, append method
dequeue - removing the element, pop method, list.pop(0) remove 0 index
isfull - set limit to the queue
isempty - whether queue is empty
used in uploading bunch of photos, printing multiple documents
can be implemented in 2 ways: list & modules
classes: dequeue - collections module
        can use- appendleft and pop, append and popleft
        2. queue module - QUEUE class
            put(item, block=True, timeout=none) #wait for free slot
            put(item, block=False, timeout=5)
            put_nowait(item) wont wait for free slot
            get(block=True, timeout=None)
            get_nowait()
works in FIFO- first in first out
"""

# queue = list()
# queue.append(10)
# queue.append(20)
# queue.append(30)
# print(queue)
# queue.pop(0) #remove from the front
# queue.pop(0)
# queue.pop(0)
# print(queue)
#
# """Method 2"""
# queue1 = list()
# queue1.insert(0, 10)
# queue1.insert(0, 20)
# queue1.insert(0, 30)
# print(queue1)
# queue1.pop()
# queue1.pop()
# queue1.pop()
# print(queue1)
# print(not queue)
# queue1.append(10)
# queue1.append(20)
# queue1.append(30)
# print(queue1[-1])
# print(queue1[0])

"""Method 3"""

import collections

q = collections.deque()  #create an empty queue
q.appendleft(10)
q.appendleft(20)
q.appendleft(30)
print(q)

q.pop()
q.pop()
q.pop()
print(q)


"""Method3b"""
q1 = collections.deque()
q1.append(10)
q1.append(20)
q1.append(30)
print(q1)
q1.popleft()
q1.popleft()
q1.popleft()
print(q1)
print(not q1)
q1.append(50)
q1.append(100)
q1.append(150)
print(q1[-1])
print(q1[0])

















