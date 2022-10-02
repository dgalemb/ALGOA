from sys import argv 
from timeit import default_timer as timer

def fib1(n):
    if n < 2:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)

def fib2(n):
    x = 1
    y = 1
    while n > 0:
        y = x + y
        x = y - x
        n = n - 1

    return x

def main():
    if len(argv) > 1:
        n = int(argv[1])
    else:
        n = 10

    start = timer()
    print(f"fib2({n}): {fib2(n)}")
    end = timer()
    print(f"computed in: {end - start:.3f}s"); 

    start = timer()
    print(f"fib1({n}): {fib1(n)}")
    end = timer()
    print(f"computed in: {end - start:.3f}s"); 


if __name__ == "__main__":
    main()


