"""
Collections - deque(double ended que)
Queue - lifoqueue class
for push operation -put
pop - get method
"""

# import collections
#
# stack = collections.deque()
# print(stack)
# stack.append(10)
# stack.append(20)
# stack.append(30)
# print(stack)
# stack.pop()
# stack.pop()
# stack.pop()
# print(stack)
#
# print(not stack)
#
# print(dir(stack)

import queue

stack = queue.LifoQueue()   #max size of element is 3
stack.put(10)
stack.put(20)
stack.put(30)
stack.put(40, timeout=1)
print(stack)
stack.get()
stack.get()
stack.get(timeout=1)
print(stack)