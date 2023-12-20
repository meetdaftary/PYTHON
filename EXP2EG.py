n = float(input("Enter the nummber (n): "))
print("Square of n is:", n ** (2))

a = float(input("Enter first number (a): "))
b = float(input("Enter second number (b): "))
a = a + b
b = a - b
a = a - b
print("After swapping:")
print("a =", a, "\nb =", b)

h = int(input("Enter height of pyramid: "))
for i in range(1, h + 1):
    for j in range(i):
        print(i, end = " ")
        print()

n = int(input("Enter the number: "))
result = 1
for i in range(1, n + 1):
    result *= i
if (n == 0):
    result = 1
print("Factorial(n) =", result)

n = int(input("Enter number of terms (n): "))
a = 0
b = 1
print(a)
print(b)
for i in range(n-2):
    c=a+b
    a=b
    b=c
    print(c)

y = int(input("Enter year: "))
if y % 4 == 0:
    if y % 100 == 0:
        if y % 400 == 0:
            print(y, "is a leap year.")
        else:
            print(y, "is not a leap year.")
    else:
        print(y, "is a leap year.") 
else:
    print(y, "is not a leap year.") 