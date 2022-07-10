"""Adjacency list for unweighted undirected graph"""


def add_node(v):
    if v in graph:
        print(v, "is already present in graph")
    else:
        graph[v] = []


def add_edge(v1, v2):
    if v1 not in graph:
        print(f"{v1} is not present in graph")
    elif v2 not in graph:
        print(v2, "is not present in graph")
    else:  #both are present
        graph[v1].append(v2)
        graph[v2].append(v1)


def delete_node(v):
    if v not in graph:
        print(f"{v} is not present in graph")
    else:  #v is present in graph
        graph.pop(v)  #deletes d key
        for i in graph:
            list1 = graph[i]
            if v in list1:
                list1.remove(v)


def delete_edge(v1, v2):
    if v1 not in graph:
        print(f"{v1} is not present in graph")
    elif v2 not in graph:
        print(v2, "is not present in graph")
    else:
        if v2 in graph[v1]:
            graph[v1].remove(v2)
            graph[v2].remove(v1)


graph = {}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_edge("A", "B")
add_edge("A", "C")
add_edge("A", "D")
add_edge("B", "D")
add_edge("B", "E")
add_edge("C", "D")
add_edge("D", "E")
print(graph)
print()
print("After deleting node")
delete_node("A")
print(graph)
print()
print("After deleting edges:")
delete_edge("B", "D")
print(graph)

