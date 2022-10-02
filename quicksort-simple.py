from random import shuffle

def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp

def quicksort(A, d, f):
    if f - d > 0:
        p = partition(A, d, f)

        # le pivot est à sa place
        quicksort(A, d, p-1)
        quicksort(A, p+1, f)

def partition(A, d, f):
     # on prend le dernier élément comme pivot
     p = A[f]
     j = d
     for i in range(d, f):
        if A[i] <= p:
            swap(A, j, i)
            j = j + 1

     swap(A, j, f)
     return j




L = list(range(10))
shuffle(L)
print(L)
quicksort(L,0, len(L) - 1)
print(L)
