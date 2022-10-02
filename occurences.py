def find_first(A, x, d, f):
    if f - d <= 0:
        if A[d] == x:
            return d
        else:
            return None
    else:     
        m = (f + d) // 2
        if x < A[m] or (m > d and A[m-1] == x):
            return find_first(A, x, d, m)
        elif x > A[m]:
            return find_first(A, x, m + 1, f)
        else:
            return m


def find_last(A, x, d, f):
    if f - d <= 0:
        if A[d] == x:
            return d
        else:
            return None
    else:     
        m = (f + d) // 2
        if x < A[m]: 
            return find_last(A, x, d, m)
        elif x > A[m] or (m < f and A[m+1] == x):
            return find_last(A, x, m + 1, f)
        else:
            return m


L = [1,2,2,3,3,3,3,3,4,4,5]
x = 3
px = find_first(L, x, 0, len(L) - 1)
print(f'première occurence de {x} dans {L}: {px}')
dx = find_last(L, x, 0, len(L) - 1)
print(f'dernière occurence de {x} dans {L}: {dx}')
print(f'nombre d\'occurences de {x} dans {L}: {dx - px + 1}')
