# Calculate the Factorial of a number

def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        return('Factorial cannot be calculated for negative numbers')
    elif n > 0:
        return n * factorial(n-1)
n=int(input("Enter a number to compute the factiorial : "))
print(factorial(n))

            





