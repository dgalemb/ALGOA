import operator
from functools import reduce

def test_list(L):
    n = len(L)
    return sum(L) == n * (n * n + 1) / 2


def test_carre(C):
    Ct = list(map(list, zip(*C))) # transpose la matrice

    # diagonales
    d1 = [C[i][i] for i in range(n)]
    d2 = [C[len(C) - 1 -i][i] for i in range(n)]

    L = C + Ct + [d1] + [d2]
    B = map(test_list, L)

    return reduce(operator.__and__, B, True)

def print_carre(C):
    n = len(C)
    for i in range(n):
        for j in range(n):
            print(f"{C[i][j]} ",end='')
        print()
    print()

def carre(C, T, k):
    # k est le numéro de la case que je souhaite remplir
    if k == n*n: 
        if test_carre(C):
            print_carre(C)
    else:
        # i est le nombre que j'essaie de mettre dans la case numéro k
        for i in range(1, n*n+1):
            if not T[i]:
                T[i] = True
                C[k // n][k % n] = i
                carre(C, T, k + 1)
                T[i] = False

n = 4
C = [[0 for i in range(n)] for j in range(n)]
T = [False for i in range(n*n+1)]
carre(C, T, 0)
