import math

def change(n, L):
    if n < 0:
        return (math.inf, []) # inf est un réel...
    elif n == 0:
        return (0, [])
    else:
        c = math.inf
        for p in L:
            (x, R) = change(n - p, L)
            if x < c:
                c = x 
                S = R 
                q = p
        
        return (1 + c, S + [q])

L = [1,3,4,10,30,40]
x = 25 
print(f'changer {x} avec {L} : {change(x, L)}')

x = 32
print(f'changer {x} avec {L} : {change(x, L)}')
