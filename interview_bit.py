
def maxSubArray(self, A):
    n = len(A)
    print A
    sum_mat = []
    maxN = A[0]
    for i, a in enumerate(A):
        sum_mat.append([0]*n)
        sum_mat[i][i] = a
        maxN = a if a > maxN else maxN

    for i in range(n):
        for j in range(i, n):
            sum_mat[i][j] = sum_mat[i][j-1] + A[j]
            maxN = sum_mat[i][j] if sum_mat[i][j] > maxN else maxN
    return maxN

print maxSubArray(1, (1, -2, 3, 4, 5))
