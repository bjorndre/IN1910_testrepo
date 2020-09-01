def add(x,y):
    return x+y

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

def sin(x,N):
    zum = 0
    for n in range(N):
        zum += ((-1)**n * x**(2*n+1))/factorial(2*n+1)
    return zum

def divide(x,y):
    return x/y

def exponential(x,y):
    return x**y

def multiplication(x,y):
    return x*y