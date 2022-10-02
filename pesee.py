from random import randint

def compare(A, d1, f1, d2, f2):
    s = 0
    for i in range(d1, f1 + 1):
        s = s + A[i]
    for i in range(d2, f2 + 1):
        s = s - A[i]

    if s > 0:
        return 1
    elif s < 0:
        return -1
    else:
        return 0

# on appelle fausse(A, 0, len(A)-1)
def fausse(A, d, f):
    if d == f:
        return d
    else:
        s = (f - d) // 3
        m1 = d + s
        # on veut m2 > m1 même si s = 0 
        # et on a bien toujours m2 <= f par construction
        m2 = d + 2*s + 1

        r = compare(A, d, m1, m1 + 1, m2)
        if r < 0:
            return fausse(A, d, m1)
        elif r > 0:
            return fausse(A, m1 + 1, m2)
        else:
            return fausse(A, m2 + 1, f)

n = 10
A = [1 for i in range(n)]
A[randint(0,n-1)] = 0

print(f'la fausse pièce dans {A} est à l\'indice: {fausse(A,0, len(A)-1)}')
