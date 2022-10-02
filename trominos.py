from random import randint

def ajoute_tromino(A, dx, dy, i, j,k):
    for a in range(2):
        x = dx + a
        for b in range(2):
            y = dy + b
            if x != i or y != j:
                A[x][y] = k

# la grille fait 2^n de côté, avec n>0, (i,j) est la case manquante
# dx, fx début, fin de la zone considérée (coord x)
# dy, fy début, fin de la zone considérée (coord y)
def trominos(A, dx, fx, dy, fy, i, j, k):
    if fx - dx + 1 == 2:
        # un tromino dont le coin gauche est en dx dy et le trou en i j
        ajoute_tromino(A, dx, dy, i, j, k)

    else:
        mx = (dx + fx + 1) // 2
        my = (dy + fy + 1) // 2

        # petit x, petit y
        a = mx - 1 # emplacement du nouveau trou si le trou i, j n'est pas dans ce carré
        b = my - 1
        if i < mx and j < my:
            # le trou i,j est dans ce carré
            # on doit mettre le trou du tromino en a, b
            ajoute_tromino(A, mx - 1, my - 1, a, b, k)
            # le trou pour le cas récursif est i, j et non a, b 
            a = i 
            b = j
        trominos(A, dx, mx - 1, dy, my - 1, a, b, k + 1)

        # petit x, grand y
        a = mx - 1
        b = my
        if i < mx and j >= my:
            ajoute_tromino(A, mx - 1, my - 1, a, b, k)
            a = i
            b = j
        trominos(A, dx, mx - 1, my, fy, a, b, k + 1)

        # grand x, petit y
        a = mx 
        b = my - 1
        if i >= mx and j < my:
            ajoute_tromino(A, mx - 1, my - 1, a, b, k)
            a = i
            b = j
        trominos(A, mx, fx, dy, my - 1, a, b, k + 1)

        # grand x, grand y
        a = mx 
        b = my 
        if i >= mx and j >= my:
            ajoute_tromino(A, mx - 1, my - 1, a, b, k)
            a = i
            b = j
        trominos(A, mx, fx, my, fy, a, b, k + 1)

n=4
N=2**n
x = randint(0,N-1)
y = randint(0,N-1)
print(f'Le plateau fait {N}x{N} et le trou est en ({x},{y})')
A = [[0 for i in range(N)] for j in range(N)] 
trominos(A, 0, N-1, 0, N-1, x, y, 1)

print()
for i in range(N):
    for j in range(N):
        print(f'{A[i][j]:2}', end='')
    print()
print()


