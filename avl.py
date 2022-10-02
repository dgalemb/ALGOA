class node:
    def __init__(self, x, p):
        self.r = x
        self.g = None
        self.d = None
        self.b = 0

def tree_height(A):
    if A == None:
        return 0
    else:
        return 1 + max(tree_height(A.g), tree_height(A.d))

def abr_print(A):
    if A != None:
        abr_print(A.g)
        print(f'{A.r} ({A.b})', end= ' ')
        abr_print(A.d)

def abr_insert(A, x):
    if A == None:
        B = node(x, None)
        
        return B
    else:
        if x < A.r:
            A.g = abr_insert(A.g, x)
        else:
            A.d = abr_insert(A.d, x)

        return A

def abr_min_parent(A, p):
    if A.g == None:
        return p
    else:
        return abr_min_parent(A.g, A)

def abr_delete(A, x):
    if A != None :
        if x == A.r:
            if A.g == None:
                return A.d
            elif A.d == None:
                return A.g
            else:
                # les deux sont non vides, on prend min arbitrairement
                # P est le parent du min de A.d
                P = abr_min_parent(A.d, A) 
                if P == A:
                    Y = A.d   # c'est directement A.d qui est le min
                else: 
                    Y = P.g   # Y est le min
                    Y.d = A.d # Y est plus petit que A.d
                    
                # Y est le min du filsd
                # le filsg de Y est forcément $\bot$
                # et Y.r est plus grand que A.g.r
                Y.g = A.g

                return Y
                
        else:
            if x < A.r:
                A.g = abr_delete(A.g, x)
            else:
                A.d = abr_delete(A.d, x)

    return A

def avl_rotate_left(A):
    R = A.d

    A.d = R.g

    R.g = A

    A.b = A.b - 1    
    if R.b > 0:
        A.b = A.b - R.b 

    R.b = R.b - 1
    if A.b < 0:
        R.b = R.b + A.b

    return R

def avl_rotate_right(A):
    R = A.g

    A.g = R.d

    R.d = A

    A.b = A.b + 1    
    if R.b < 0:
        A.b = A.b - R.b 

    R.b = R.b + 1
    if A.b > 0:
        R.b = R.b + A.b

    return R


def avl_balance(A):
    R = A
    if A != None:
        if A.b == 2:
            if A.d.b < 0:
                A.d = avl_rotate_right(A.d)
            
            R = avl_rotate_left(A)
        elif A.b == -2:
            if A.g.b > 0:
                A.g = avl_rotate_left(A.g)
            
            R = avl_rotate_right(A)

    return R

def avl_insert(A, x, p, bfu):
    retrace = (p != None)

    if A == None:
        B = node(x, p)
    else:
        if x < A.r:
            A.g = avl_insert(A.g, x, A, -1)
        else:
            A.d = avl_insert(A.d, x, A, +1)
        
        B = avl_balance(A)
        if B.b == 0:
            retrace = False

    if retrace:
        p.b = p.b + bfu

    return B



X = [5, 4, 7, 8, 3, 1]
Y = [1, 3, 4, 5, 7, 8]
Z = [1, 3, 8, 6, 5, 4]

A = None
for x in Z:
    #A = abr_insert(A, x)
    A = avl_insert(A, x, None, 0)
    abr_print(A)
    print(f'\nhauteur: {tree_height(A)}')

A = abr_delete(A, 5)
abr_print(A)
print(f'\nhauteur: {tree_height(A)}')
#A = avl_rotate_left(A)
#abr_print(A)
#print(f'\nhauteur: {tree_height(A)}')
