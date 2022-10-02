import math

# top-down avec mémoïsation
def matrix_chain_desc(d, m, i, j):
    if m[i][j] != -1:
        return m[i][j]
    else:
        if i == j:
            m[i][j] = 0
        else:
            m[i][j] = math.inf
            for k in range(i, j):
                xk = matrix_chain_desc(d, m, i, k) + matrix_chain_desc(d, m, k + 1, j) + d[i - 1] * d[k] * d[j]
                if xk < m[i][j]:
                    m[i][j] = xk

        return m[i][j]

# bottom-up 
def matrix_chain_asc(d, n):
    m = [[-1 for i in range(n + 1)] for j in range(n + 1)]
    r = [[-1 for i in range(n + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        m[i][i] = 0

    # par nombre de matrices dans la chaîne croissant
    for s in range(2, n + 1):
        for i in range(1, n - s + 2):
            j = i + s - 1
            m[i][j] = math.inf 
            for k in range(i, j):
                xk = m[i][k] + m[k + 1][j] + d[i - 1] * d[k] * d[j]
                if xk < m[i][j]:
                    m[i][j] = xk
                    r[i][j] = k
            
    return (m, r)

# un simple parcours infixe
def print_expr(i, j, r):
    if i == j:
        print(i, end='')
    else:
        k = r[i][j]
        print('(', end='')
        print_expr(i, k, r)
        print(') * (', end='')
        print_expr(k + 1, j, r)
        print(')', end='')

n = 6
d = [30, 35, 15, 5, 10, 20, 25]

m = [[-1 for i in range(n + 1)] for j in range(n + 1)]
print(matrix_chain_desc(d, m, 1, n))

m, r = matrix_chain_asc(d, n)
print(m[1][n])

print_expr(1, n, r)
print()

