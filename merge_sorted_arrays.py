
def merge_sorted(a, b):
    ai, bi = 0, 0
    sorted_list = []
    while ai < len(a) and bi < len(b):
        if a[ai] < b[bi]:
            sorted_list.append(a[ai])
            ai += 1
        else:
            sorted_list.append(b[bi])
            bi += 1
    while ai < len(a):
        sorted_list.append(a[ai])
        ai += 1
    while bi < len(b):
        sorted_list.append(b[bi])
        bi += 1

    return sorted_list

print merge_sorted([3, 4, 6, 10, 11, 15], [1, 5, 8, 12, 14, 19])
