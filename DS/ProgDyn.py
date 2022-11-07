import time

def fact(n):

    if n == 0 or n == 1:
        return 1 

    return n*fact(n-1)

def CatalanBrut(n):

    return int(fact(2*n)/(fact(n+1) * fact(n)))


def fibmemo(n, table = {}):

    if n <= 1:
        return n

    else:
        if n in table:
            return table[n]

        else:

            table[n] = fib(n - 1, table) + fib(n - 2, table)
            return table[n]

def fibrec(n):

    if n <= 1:
        return n
    else:
        return fib(n-1)+fib(n-2)

def fibasc(n):

    if n <= 1:
        return n

    a = 0
    b = 1

    for k in range(n):
        temp = a + b
        a = b
        b = temp
    
    return b

