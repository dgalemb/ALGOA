from random import shuffle

def sort(A, n):
    for i in range(1, n):
        insert(i, A)

def insert(x, A):
    key = A[x]

    j = x - 1
    while j >= 0 and A[j] > key:
        A[j + 1] = A[j]
        j = j - 1

    A[j + 1] = key

L = list(range(10))
shuffle(L)
print(*L)

sort(L, 10)
print(*L)


