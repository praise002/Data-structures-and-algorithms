"""
Modified version of queues in which element is associated with a priority
can make:
low- high priority
or
high - high priority
or
you take the element itself as the priority
    how to implement priority
        - list: sort the list
        - priority queue class from queue module: use binary heap data structure
"""

q = list()
q.append(10)
q.append(40)
q.append(20)
q.sort()
print(q)
q.pop(0)
print(q)   #not the best way to implement priority queue



"""Part 2"""
import queue

q1 = queue.PriorityQueue()
q1.put(10)
q1.put(60)
q1.put(20)
q1.put(40)
q1.put(40)
print(q1.get())

q3 = list()
q3.append((1, "alexa"))
q3.append((4, "alex"))
q3.append((2, "al"))  #in a tuple
q3.sort(reverse=True)
print(q3)
print(q3.pop(0))