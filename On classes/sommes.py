def sommes(A, n):
    R = [[0 for i in range(n)] for j in range(n)]
    P = [[0 for i in range(n)] for j in range(n)]

    for j in range(n):
        R[n - 1][j] = A[n-1][j]
        P[n - 1][j] = j

    for i in range(n-1, 0, -1):
        for j in range(n):
            s = R[i][j]
            k = j
            if j > 0 and R[i][j - 1] > s:
                s = R[i][j - 1]
                k = j - 1

            if j < n - 1 and R[i][j + 1] > s:
                s = R[i][j + 1]
                k = j + 1

            R[i - 1][j] = A[i - 1][j] + s
            P[i - 1][j] = k

    return (R[0], P)

def print_matrix(P, n):
    for i in range(n):
        for j in range(n):
            print(f'{P[i][j]}', end='')
        print()
    print()


n = 4
A = [[4, 5, 8, 9],
     [7, 3, 4, 6],
     [1, 5, 2, 5],
     [9, 2, 6, 4]]

print_matrix(A, n)
R, P = sommes(A, n)

# P donne pour chaque case le meilleur successeur
# on calcule X qui pour chaque colonne j en déduit 
# le chemin en partant de la case j en haut
X = [[0 for i in range(n)] for j in range(n)]
for j in range(n):
    cur = j
    for i in range(n):
        X[i][j] = cur
        cur = P[i][cur]

print()
print(R)
print_matrix(P, n)
print()
print_matrix(X, n)

