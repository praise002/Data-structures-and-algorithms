import heapq

heap = list()
heapq.heappush(heap, 10)
heapq.heappush(heap, 1)  #it follows min heap property
heapq.heappush(heap, 5)
heapq.heappop(heap)  #removes d smallest value and deletes it
print(heap)

list1 = [1, 3, 5, 2, 4, 6]
heapq.heapify(list1)
heapq.heappushpop(list1, 89)  #removes min val & inserts dat item, push->pop
heapq.heapreplace(list1, 100)  #pop->push
print(list1)
print(heapq.nsmallest(2, list1))
print(heapq.nlargest(3, list1))

"""Implementing priority"""

lst1 = [(1, "ria"), (4, "sia"), (3, "gia")]
heapq.heapify(lst1)
print(lst1)
for i in range(len(lst1)):
    print(heapq.heappop(lst1))