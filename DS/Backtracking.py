def printall(L, n):

    gr = [['.' for _ in range(n)] for _ in range(n)]

    for (i,j) in L:
        gr[i][j] = 'R'

    return gr

def aligned(L, i, j):

    for (m, n) in L:
        if m == i or n == j or abs(i - m) == abs(j - n):
            return True
    return False

def queens(n, i = 0, L = []):

    if i == n:
        res = printall(L, n)
        for r in res:
            print(r)
        print('\n')
    else:
        for j in range(n):
            if not aligned(L, i, j):
                L2 = L[:]
                L2.append((i, j))
                queens(n, i + 1, L2)

#print(queens(4))

