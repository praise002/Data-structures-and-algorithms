""""weighted directed graph"""


def add_node(v):
    global node_count
    if v in nodes:
        print("The node is already present in the graph")
    else:
        node_count = node_count + 1
        nodes.append(v)
        for col in graph:
            col.append(0)  #inner loop
        temp = []  #new row
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)


def add_edge(v1, v2, cost):
    if v1 not in nodes:
        print(v1, "is not present in graph")
    elif v2 not in nodes:
        print(v2, "is not present in graph")
    else:  #both are present add edge
        #find d index of v1&v2
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = cost


def delete_node(v):
    global node_count
    if v not in nodes:
        print(v, "is not present in the graph")
    else:  #node is present
        index1 = nodes.index(v)
        node_count = node_count - 1
        nodes.remove(v)  #remove v from d nodes
        graph.pop(index1)  #to remove row
        for i in graph:
            i.pop(index1)  #remove column


def delete_edge(v1, v2):
    if v1 not in nodes:
        print(v1, "is not present in graph")
    elif v2 not in nodes:
        print(v2, "is not present in graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 0


def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j], "<2"), end=" ")
        print()


graph = []  #to store d matrix
nodes = []  #to store nodes
node_count = 0
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_node("F")
add_node("G")
add_edge("A", "B", 10)
add_edge("A", "C", 5)
add_edge("B", "D", 7)
add_edge("B", "E", 8)
add_edge("F", "C", 1)
add_edge("F", "G", 3)
add_edge("G", "D", 2)
print(nodes)
print(graph)
print_graph()
print()
print("After deleting nodes:")
delete_node("A")
print(nodes)
print(graph)
print()
print("After deleting edges:")
delete_edge("B", "D")
print(nodes)
print(graph)