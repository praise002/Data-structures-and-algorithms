stack = []


def push():
    if len(stack) == n:
        print('List is full')
    else:
        element = input('Enter the element: ')
        stack.append(element)
        print(stack)


def pop_element():
    if not stack:
        print('Stack is empty!')
    else:
        e = stack.pop()
        print("removed element:", e)
        print(stack)


def peek():
    if not stack:
        print('Stack is empty!')
    else:
        p = stack[-1]
        print("Present at the top:", p)


n = int(input("Limit of stack: "))
while True:
    print("Select operation 1. push 2. pop 3. peek 4. quit")
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop_element()
    elif choice == 3:
        peek()
    elif choice == 4:
        break
    else:
        print("Enter the correct operation!")