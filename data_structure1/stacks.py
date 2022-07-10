"""
An ordered collection of items
LIFO - last in first out
FILO - first in last out
Basic operations - push, pop, peek or top, isempty
push- adds element to the stack
pop - remove element from the stack
peek - give you the element present at the top
isempty - tells you whether stack is empty or not
Are considered as backbone of data structure
Used for forward and backward movement in web browsers
We can implement data structures using - list, modules
push - append , it adds element to the end of the list
pop - pop, it removes element from the end of the list
"""

stack = list()
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)
stack.pop()
stack.pop()
stack.pop()
print(stack)
print(len(stack) == 0)
print(not stack)  # to check isempty

stack.append(10)
stack.append(20)
stack.append(30)
print(stack[-1])  #for peek




