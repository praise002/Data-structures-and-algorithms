import queue

q = queue.Queue()
q.put(10)
q.put(30)
q.put(50)
print(q)

q.get()
q.get()
q.get()
# q.get(timeout=1)
print(q)