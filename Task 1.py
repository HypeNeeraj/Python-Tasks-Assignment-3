num = int(input("Enter the Number: "))

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)

print(f"Factorial of {num} is {factorial(num)}")
