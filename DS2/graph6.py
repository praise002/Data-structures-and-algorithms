"""Using adjacency list for unweighted directed graph"""


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


graph = {}   #create dict
add_node("A")
add_node("B")
add_node("C")
add_edge("A", "B")
add_edge("A", "C")
print(graph)

print("After deleting:")
delete_edge("A", "C")
print(graph)
