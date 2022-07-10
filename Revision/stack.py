stack = list()  #last in first out
print(not stack)
stack.append("www.google.com")
stack.append("www.forexfactory.com")
stack.append("www.fxstreet.com")
stack.append("www.fxstreet/news.com")
print(stack)
print(stack[-1])  #peek
print(len(stack) == 0)
print(not stack)  #empty

stack.pop()
stack.pop()
stack.pop()
stack.pop()
print(stack)

"""Part 2"""


# def push():
#     if len(stack) == n:
#         print("List is full!")
#     else:
#         element = int(input("Enter the element: "))
#         stack.append(element)
#         print(stack)
#
#
# def pop_element():
#     if len(stack) == 0:
#         print("Can't pop from an empty list.")
#     else:
#         e = stack.pop()
#         print("Removed element", e)
#
#
# def peek():
#     if not stack:
#         print("Stack is empty")
#     else:
#         p = stack[-1]
#         print("Present at the top", p)
#
#
# stack = list()
# n = int(input("Limit of stack: "))
# while True:
#     print("Select operation 1. push 2. pop 3. peek 4. quit")
#     choice = int(input())
#     if choice == 1:
#         push()
#     elif choice == 2:
#         pop_element()
#     elif choice == 3:
#         peek()
#     elif choice == 4:
#         break
#     else:
#         print("Enter the correct operation!")


"""Part 3"""
import collections

stack = collections.deque([])  #create an empty list
print(stack)
print(not stack)
print(len(stack))
stack.append("pencil")
stack.append("biro")
stack.append("cheese")
# stack.reverse()
# stack.remove("biro")
print(not stack)
print(stack)
print(len(stack))
print(stack[-1])
print(dir(stack))

stack.pop()
stack.pop()
stack.pop()
# stack.pop()
print(stack)


"""Part 4"""
print()
stack = collections.deque([])
stack.appendleft(20)
stack.appendleft(30)
stack.appendleft(40)
print(stack)
print(len(stack))
print(not stack)
print(stack[0])

stack.popleft()
stack.popleft()
print(stack)

"""Part 5"""
import queue

s = queue.LifoQueue()
s.put(30)
s.put(50)
print(s)