"""Using adjacency list for weighted undirected graph"""


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
            dfs(i[0], visited, graph)  #call it recursively bcus we ar doing d 1st step again
            #d 1[0] means to only print d 0 index of i


visited = set()  #to avoid repitition


graph = {}   #create dict
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

dfs("A", visited, graph)
