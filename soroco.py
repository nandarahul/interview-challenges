import sys
min_cost = sys.maxint


def do_stuff(visited):
    # print "hello"
    global A, min_cost
    B = []
    for v in visited:
        B.append(A[v[0]][v[1]])
    B.sort()
    mid = len(B)/2
    if len(B) % 2:
        median = B[mid]
    else:
        median = int((B[mid-1]+B[mid])/2)
    ans = 0
    for b in B:
        ans += abs(b-median)
    print B
    if ans < min_cost:
        print B
        min_cost = ans

import copy
def depth_first(source, mvisited):
    # print "j"
    global N, M
    visited = copy.copy(mvisited)
    if source[0] in (-1, N) or source[1] in (-1, M) or source in visited:
        # print "FUK"
        return
    visited.add(source)
    if source == (N-1, M-1):
        do_stuff(visited)
        return
    depth_first((source[0]+1, source[1]), visited)
    depth_first((source[0]-1, source[1]), visited)
    depth_first((source[0], source[1]+1), visited)
    depth_first((source[0], source[1]-1), visited)


N, M = map(int, raw_input().split())
A = []
for _ in range(N):
    row = map(int, raw_input().split())
    A.append(row)

depth_first((0,0), set([]))
print min_cost
