def matricMul(A, B, p, q, r):

    C = [[0 for y in range(q)] for o in range(p)]

    for i in range(p):

        for j in range(q):
        
            C[i][j] = 0

            for k in range(r):

                    C[i][j] = C[i][j] + A[i][j]

    
    return C

A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[1,2,3],[4,5,6],[7,8,9]]
p = 3
q = 3
r = 3

print(matricMul(A, B, p, q, r))