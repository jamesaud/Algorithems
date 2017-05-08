from __future__ import print_function
# Enter your code here. Read input from STDIN. Print output to STDOUTfrom __future__ import print_function
#!/usr/bin/env python
import sys

from Queue import *
def bfs_result(src, graph):
    adjacency_List = {src: 0}
    #bfs
    queue = Queue()
    queue.put(src)
    while (not queue.empty()):
        element = queue.get()
        distance = adjacency_List[element] + 6
        for neighbor in graph[element]:
           
            if (neighbor in adjacency_List):
                continue
            adjacency_List[neighbor] = distance
            queue.put(neighbor)
    return adjacency_List


def result(src, v, distances):
    for i in range(1, v + 1):
        if (i == src):
            continue
        if i in distances:
            print(distances[i], end=" "),
        else:
            print(-1, end=" "),
    print()


no_of_cases = int(input())
graph = [0]
for i in range(no_of_cases):
    graph = [0]
    vertex,edges =map(int, raw_input().split())
    dum_vertex=vertex
    dum_edges=edges
    while (int(vertex)> 0):
        graph.append([])
        vertex-= 1

    while (int(edges)> 0):
        (x, y) = map(int, raw_input().split())
        graph[x].append(y)
        graph[y].append(x)
        edges -= 1

    src_node = int(raw_input())
    adjacency_List = bfs_result(src_node, graph)
    result(src_node, dum_vertex, adjacency_List)
