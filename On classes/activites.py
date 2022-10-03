n = 11
D = [1, 3, 0, 5, 3, 5, 6,  7,  8,  2,  12]
F = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]

def f(n):
    return F[n]

def activites(D, F, n):
    # tri selon F
    A = list(range(n))
    A.sort(key=f)
    resultat = [A[0]]
    date = F[A[0]]
    
    for i in range(n):
        if D[A[i]] >= date:
            date = F[A[i]]
            resultat.append(A[i])
        
    return resultat

print(activites(D, F, n))
