import sys

def traverse(tree, root_index, u, l, descendantSeen):
    if root_index == u:
        descendantSeen = True
    if l == 0:
        if descendantSeen:
            return tree[root_index][0]
        else:
            return 0
    score_sum = 0
    for child_index in tree[root_index][1]:
        score_sum += traverse(tree, child_index, u, l-1, descendantSeen)
    return score_sum

def compute_score_sum(tree, u, l):
    if l <= 0:
        return 0
    return traverse(tree, 1, u, l-1, False)

T = int(raw_input())
while T:
    T -= 1
    N, Q = raw_input().split()
    N, Q = int(N), int(Q)
    tree = [[0, []]]
    scores = sys.stdin.readline().split()
    for i, s in enumerate(scores):
        tree.append([int(s), []])
    for _ in range(N-1):
        i, j = sys.stdin.readline().split()
        i, j = int(i), int(j)
        tree[i][1].append(j)
    for _ in range(Q):
        u, l = sys.stdin.readline().split()
        u, l = int(u), int(l)
        print compute_score_sum(tree, u, l)
