
def aligned(L, i, j):
    for (k,l) in L:
        if k == i or l == j or abs(k - i) == abs(l - j):
            return True

    return False

def print_queens(L):
    print(L)
    n = len(L)
    B = [['.' for i in range(n)] for j in range(n)]

    for (i, j) in L:
        B[i][j] = 'Q'

    for i in range(n):
        for j in range(n):
            print(f"{B[i][j]} ", end='')
        print()
    print()

def queen(L, i, n):
    if i == n:
        print_queens(L)
    else:
        for j in range(n):
            if not aligned(L, i, j):
                L2 = L[:]
                L2.append((i, j))
                queen(L2, i + 1, n)

n = 20
L = []
queen(L, 0, n)

