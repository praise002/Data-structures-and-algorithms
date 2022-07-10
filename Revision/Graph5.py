"""Adjacency list for weighted undirected graph"""
import collections


def add_node(v):
    if v in graph:
        print(v, "is already present in graph")
    else:
        graph[v] = []


def add_edge(v1, v2, cost):
    if v1 not in graph:
        print(f"{v1} is not present in graph")
    elif v2 not in graph:
        print(v2, "is not present in graph")
    else:  #both are present
        temp = [v1, cost]
        temp1 = [v2, cost]
        graph[v1].append(temp1)
        graph[v2].append(temp)


def delete_node(v):
    if v not in graph:
        print(f"{v} is not present in graph")
    else:  #v is present in graph
        graph.pop(v)  #deletes d key
        for i in graph:
            list1 = graph[i]
            if v in list1:
                list1.remove(v)


def delete_edge(v1, v2, cost):
    if v1 not in graph:
        print(f"{v1} is not present in graph")
    elif v2 not in graph:
        print(v2, "is not present in graph")
    else:
        temp = [v1, cost]
        temp1 = [v2, cost]
        if temp1 in graph[v1]:
            graph[v1].remove(temp1)
            graph[v2].remove(temp)
        else:
            print(cost, "is not present in", v1, "to", v2)


def dfs(node, visited, graph):
    if node not in graph:
        print(node, "is not present in graph")
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            dfs(i[0], visited, graph)


def dfs_iterative(node, visited, graph):   #uses stack data structure
    if node not in graph:
        print(node, "is not present in graph")
        return
    stack = list()
    stack.append(node)
    while stack:  #stopping condition is wen stack bcums empty
        current = stack.pop()
        if current not in visited:
            print(current)
            visited.add(current)
            for i in graph[current]:
                stack.append(i[0])


def bfs_iterative(node, visited, graph):
    if node not in graph:
        print(node, "is not present in graph")
        return
    queue = collections.deque()  #initialize a queue
    queue.append(node)
    while queue:
        current = queue.popleft()
        if current not in visited:
            print(current)
            visited.add(current)
            for i in graph[current]:
                queue.append(i[0])


visited = set()
graph = {}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_edge("A", "B", 10)
add_edge("A", "C", 5)
add_edge("A", "D", 4)
add_edge("B", "D", 7)
add_edge("B", "E", 2)
add_edge("C", "D", 1)
add_edge("D", "E", 2)
print(graph)
# print()
# print("After deleting node")
# delete_node("A")
# print(graph)
# print()
# print("After deleting edges:")
# delete_edge("B", "D", 7)
# print(graph)
print()
# print("DFS:")
# dfs("A", visited, graph)
# print("DFS2:")
# dfs("A", visited, graph)
print("BFS:")
dfs("A", visited, graph)

