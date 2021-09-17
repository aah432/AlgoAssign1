# Amber Harding Assign 1

def fib(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        print("+ 0 ")
        return 0
    elif n == 1:
        print("+ 1 ")
        return 1
    else:
        return fib(n - 1) + fib(n-2)


def fibItHelper(n, a, b):
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return fibItHelper(n-1, a, b) + fibItHelper(n - 2, a, b)


def fibIt(n):
    return fibItHelper(n, 0, 1)


if __name__ == '__main__':
    print("Calling fib on 11")
    print(fib(11))
    print("Calling fibIt on 11")
    print(fibIt(110))

