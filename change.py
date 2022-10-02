import math

def change(n, L):
    r = [0 for i in range(0, n + 1)] 
    for i in range(1, n + 1):
        c = math.inf
        for p in L:
            if i - p >= 0 and r[i - p] < c:
                c = r[ i - p]
        
        r[i] = 1 + c
    
    return r[n]


L = [1,3,4,10,30,40]
x = 25 
print(f'changer {x} avec {L} : {change(x, L)}')

x = 32
print(f'changer {x} avec {L} : {change(x, L)}')

x = 1000
print(f'changer {x} avec {L} : {change(x, L)}')
