"""Using adjacency list for unweighted undirected graph"""


def add_node(v):  #v is new node
    if v in graph:   #check if node exist in graph
        print(v, "is already present in graph.")
    else:
        graph[v] = []  #add new node to d dict rep it wit an empty list


def add_edge(v1, v2):  #2 vertices to add an edge
    #check if given vertices is present in graph
    if v1 not in graph:
        print(v1, "is not present n graph.")
    elif v2 not in graph:
        print(v2, "is not present in graph.")
    else:   #v1&v2 is present in graph
        graph[v1].append(v2)
        graph[v2].append(v1)


def delete_node(v):  #works for unweighted, directed & undirected graph
    if v not in graph:  #check if v is present in graph
        print(v, "is not present in graph.")
    else:  #v is present in graph
        graph.pop(v)  #it will delete d key-value pair
        for i in graph:  #reps key in graph
            list1 = graph[i]  #pointing to d value of d keys
            if v in list1:
                list1.remove(v)  #removes d node from d list


def delete_edge(v1, v2):
    if v1 not in graph:  #check if given nodes is present in graph
        print(v1, "is not present in graph")
    elif v2 not in graph:
        print(v2, "is not present in graph")
    else:   #d 2 vertices is present
        if v2 in graph[v1]:
            graph[v1].remove(v2)  #v1 is to access d key
            graph[v2].remove(v1)


def dfs(node, visited, graph):    #starting node
    #visit d starting node
    #visit d adjacent starting node
    if node not in graph:
        print(node, "is not in graph!")
        return   #break out of d loop
    if node not in visited:
        print(node)  #visit d node
        visited.add(node)  #add it to visited
        for i in graph[node]:
            dfs(i, visited, graph)  #call it recursively bcus we ar doing d 1st step again


def bfs(node, visited, graph):  #it considers all neigbors first
    #visit starting node
    #visit adjacent starting node
    if node not in graph:
        print(node, "is not present in graph!")
        return
    queue = list()
    queue.append(node)
    while queue:  #stopping condition
        current = queue.pop(0)
        if current not in visited:
            print(current)  # visit the node
            visited.add(current)  # add to visited
            for neigbour in graph[current]:
                bfs(neigbour, visited, graph)


visited = set()  #to avoid repitition

graph = {}   #create dict
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_edge("A", "B")
add_edge("A", "C")
add_edge("A", "D")
add_edge("C", "D")
add_edge("B", "D")
add_edge("D", "E")
add_edge("B", "E")
print(graph)

# delete_node("A")
# delete_node("C")
# delete_node("F")
# print("After deleting:")
# print(graph)

print()
# delete_edge("B", "C")
# print(graph)

# dfs("A", visited, graph)
bfs("A", visited, graph)
#work on recursive for bfs
