def factorial(n):
    if n == 1:
        return 1
    else:
        return(n * factorial(n - 1))
    
num = 3
print("factorial of", num, "is", factorial(num))