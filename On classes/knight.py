def moves(B, i, j):
    n = len(B)
    deps = [(2,1), (-2,1), (2, -1), (-2 , -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    L = []
    for (x, y) in deps:
        if i+x >= 0 and i + x < n and j + y >= 0 and j + y < n and B[i + x][j + y] == 0:
            L.append((i+x, j+y))

    return L

def print_board(B):
    n = len(B)
    for i in range(n):
        for j in range(n):
            print(f"{B[i][j]:2d} ",end='')
        print()
    print()



def knight(B, i, j, k):
    if k == n*n + 1:
        print_board(B)
    else:
        for (x, y) in moves(B, i, j):
            B[x][y] = k
            knight(B, x, y, k + 1)
            B[x][y] = 0





n = 8
B = [[0 for i in range(n)] for j in range(n)]
B[0][0] = 1

knight(B, 0, 0, 2)

