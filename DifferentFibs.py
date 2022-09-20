#Top-Down Fib

def top_down_fib(n, L):

    if n == 0 or n == 1:
        L.append(n)
        return 1

    if L[n] != 0:
        return L[n]

    L[n] = top_down_fib(n - 1, L) + top_down_fib(n - 2, L)

    return L[n]

#print(top_down_fib(k, [0 for x in range(k+1)]))


#Recursive Fib

def rec_fib(n):

    if n == 0 or n ==1:
        return n

    else:
        return rec_fib(n-1) + rec_fib(n-2)

for k in range(500):
    print(top_down_fib(k, [0 for x in range(k+1)]))