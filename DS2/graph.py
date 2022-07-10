"""Weighted undirected graph"""


def add_node(v):
    global node_count
    #check if v or node is present in d node list
    if v in nodes:
        print("The node is already present in the graph!")
    else:
        node_count = node_count + 1  #increment node count
        nodes.append(v)  #add the node to the node list
        for n in graph:
            n.append(0)  #inner loop, add a new column
        temp = []  #new row
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)  #append new row to graph


def add_edge(v1, v2, cost):  #v1 is node1
    if v1 not in nodes:
        print(v1, "is not present in the graph!")
    elif v2 not in nodes:  #2nd vertex
        print(v2, "is not present in the graph.")
    else:  #v1 & v2 is present in d graph
        #find d index of v1&v2
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        # graph[index1][index2] = 1
        # graph[index2][index1] = 1  #undirected unweighted graph
        graph[index1][index2] = cost
        graph[index2][index1] = cost


def delete_node(v):  #works for all
    global node_count
    if v not in nodes:  #check if node is present
        print(v, "is not present in the graph!")
    else:  #v is present in d graph
        index1 = nodes.index(v)  #d index of d node
        node_count = node_count - 1  #it is decreased because a node is removed
        nodes.remove(v)
        graph.pop(index1)  #to remove row
        for i in graph:  #it reps inner list
            i.pop(index1)


def delete_edge(v1, v2):  #works for undirected graph, weighted & unweighted
    if v1 not in nodes:
        print(v1, "is not present in graph.")
    elif v2 not in nodes:
        print(v2, "is not present in graph!")
    else:  #d 2 vertix is present
        index1 = nodes.index(v1)  #find its index
        index2 = nodes.index(v2)
        graph[index1][index2] = 0  #make it 0
        graph[index2][index1] = 0


def print_graph():
    for i in range(node_count):
        for j in range(node_count):  #nested loop
            print(format(graph[i][j], "<3"), end=" ")
        print()


nodes = []
graph = []  # to store the matrix
node_count = 0


print("Before adding nodes:")
print(nodes)
print(graph)

add_node("A")
add_node("B")
add_node("C")
add_edge("A", "B", 10)
add_edge("A", "C", 5)
print("After adding nodes:")
print(nodes)
print(graph)
print_graph()

# delete_node("A")
# delete_node("D")
# print("After deleting:")
# print(nodes)
# print(graph)
# print_graph()

delete_edge("A", "C")
print(graph)
print_graph()


