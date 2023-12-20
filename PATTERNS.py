def pascal(n):
   for i in range(n+1):
      for j in range(n-i):
         print(' ', end='')

      C = 1
      for j in range(1, i+1):
         print(C, ' ', sep='', end='')
         C = C * (i - j) // j
      print()
pascal(5)
print("\n")


def print_diamond(n):
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        stars = '* ' * i
        print(spaces , stars)
    for i in range(n - 1, 0, -1):
        spaces = ' ' * (n - i)
        stars = '* ' * i
        print(spaces , stars)
print_diamond(5)
print("\n")