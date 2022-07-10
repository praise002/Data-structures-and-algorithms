import collections


def add_node(v):  #v is new node
    if v in graph:   #check if node exist in graph
        print(v, "is already present in graph.")
    else:
        graph[v] = []  #add new node to d dict rep it wit an empty list


def add_edge(v1, v2, cost):  #2 vertices to add an edge
    #check if given vertices is present in graph
    if v1 not in graph:
        print(v1, "is not present n graph.")
    elif v2 not in graph:
        print(v2, "is not present in graph.")
    else:   #v1&v2 is present in graph
        list1 = [v2, cost]
        list2 = [v1, cost]
        graph[v1].append(list1)
        graph[v2].append(list2)


def delete_node(v):
    if v not in graph:  #check if v is present in graph
        print(v, "is not present in graph.")
    else:  #v is present in graph
        graph.pop(v)  #it will delete d key-value pair
        for i in graph:  #reps key in graph
            list1 = graph[i]  #pointing to d value of d keys
            for j in list1:
                if v == j[0]:
                    list1.remove(j)
                    break


def delete_edge(v1, v2, cost):
    if v1 not in graph:  #check if given nodes is present in graph
        print(v1, "is not present in graph")
    elif v2 not in graph:
        print(v2, "is not present in graph")
    else:   #d 2 vertices is present
        temp = [v1, cost]
        temp1 = [v2, cost]
        if temp1 in graph[v1]:
            graph[v1].remove(temp1)  #v1 is to access d key
            graph[v2].remove(temp)

        else:
            print(cost, "is not present in", v1, "to", v2)


def dfs_iterative(node, graph):  #pass visited inside d fn if you define it outside d fn
    visited = set()
    if node not in graph:
        print(node, "is not present in graph.")
        return
    #push starting node to stack
    #pop starting node
    #check if pop element is in visited, if not add it, print it
    stack = list()
    stack.append(node)  #add starting node
    while stack:  #it becomes false when stack becomes empty
        current = stack.pop()
        if current not in visited:
            print(current)
            visited.add(current)
            for i in graph[current]:  # e.g graph[a]
                stack.append(i[0])


def bfs_iterative(node, graph):
    visited = list()  #list for visited nodes
    if node not in graph:
        print(node, "is not present in graph.")
        return
    queue = collections.deque([])  # initialize a queue
    queue.append(node)  #add starting node
    while queue:  #becomes false when queue is empty
        current = queue.popleft()
        if current not in visited:
            print(current)  #visit current
            visited.append(current)  #add current to visited
            for i in graph[current]:
                queue.append(i[0])


graph = {}  #create dict
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_edge("A", "B", 10)
add_edge("A", "C", 5)
add_edge("A", "D", 4)
add_edge("C", "D", 1)
add_edge("B", "D", 7)
add_edge("D", "E", 2)
add_edge("B", "E", 3)
print(graph)

print("\n")
# print("After deletion:")
# delete_node("A")
# delete_node("B")
# print(graph)

# delete_edge("C", "A", 5)
# print(graph)

# dfs_iterative("E", graph)
bfs_iterative("E", graph)



