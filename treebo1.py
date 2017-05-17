import sys

M = int(raw_input())
graph = sys.stdin.readline().split()
graph = [int(g) for g in graph]
graph = [0] + graph
K = int(raw_input())
while K:
    K -= 1
    query = sys.stdin.readline().split()
    query = [int(q) for q in query]
    if query[0] == 1:
        traversedSet = set([])
        current_node = query[1]
        while True:
            if graph[current_node] == 0:
                print current_node
                break
            if graph[current_node] in traversedSet:
                print "LOOP"
                break
            traversedSet.add(current_node)
            current_node = graph[current_node]
    elif query[0] == 2:
        graph[query[1]] = 0
