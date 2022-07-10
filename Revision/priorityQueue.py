import queue

q1 = queue.PriorityQueue()  #it has to be sorted
# queue.Full
# queue.Empty
q1.put((10, "Red balls"))
q1.put((8, "Pink balls"))
q1.put((5, "White balls"))
q1.put((4, "Green balls"))
while not q1.empty():
    item = q1.get(timeout=2)
    print(item, end=" ")  #best method


"""Method 2"""
student = list()
student.append((5, "Nick"))
student.append((1, "Rohan"))
student.append((3, "Jack"))
student.sort(reverse=True)
while student:  #wen list is empty it wil break
    t = student.pop(0)
    print()
    print(t, end=" ")
