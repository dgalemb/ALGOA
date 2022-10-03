def dicho(A, x, d, f):
    if f - d <= 0:
        return (A[d] == x) 
    else:     
        m = (f + d) // 2
        if x == A[m]:
            return True
        else:
            if x < A[m]:
                return dicho(A, x, d, m)
            else:
                return dicho(A, x, m + 1, f)

L = list(range(1,10))
x = 1
print(f'{x} est dans {L}: {dicho(L, x, 0, len(L) - 1)}')
x = 0
print(f'{x} est dans {L}: {dicho(L, x, 0, len(L) - 1)}')
x = 3
print(f'{x} est dans {L}: {dicho(L, x, 0, len(L) - 1)}')
x = 9
print(f'{x} est dans {L}: {dicho(L, x, 0, len(L) - 1)}')
x = 10
print(f'{x} est dans {L}: {dicho(L, x, 0, len(L) - 1)}')
