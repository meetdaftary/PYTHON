def print_square(n):
    for i in range(n):
        print('a ' * n)
print_square(5)
print("\n")

def print_triangle(n):
    for i in range(1, n + 1):
        print('* ' * i)
print_triangle(7)
print("\n")

def print_inverted_triangle(n):
    for i in range(n, 0, -1):
        print('* ' * i)
print_inverted_triangle(6)
print("\n")

def print_pyramid(n):
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        stars = 'A ' * i
        print(spaces + stars)
print_pyramid(5)

print("\n")

def print_diamond(n):
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        stars = '* ' * i
        print(spaces + stars)
    for i in range(n - 1, 0, -1):
        spaces = ' ' * (n - i)
        stars = '* ' * i
        print(spaces + stars)
print_diamond(5)
print("\n")

def print_pattern(n):
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        characters = ' '.join(chr(ord('A') + j) for j in range(i))
        print(spaces + characters)

    for i in range(n - 1, 0, -1):
        spaces = ' ' * (n - i)
        characters = ' '.join(chr(ord('A') + j) for j in range(i))
        print(spaces + characters)

print_pattern(4)

print("\n")

def print_pattern(n):
    current_char = 'A'

    for i in range(0, n ):
        spaces = ' ' * (n - i)
        characters = ''.join(chr(ord(current_char) + j) for j in range(i * 2 - 1))
        print(spaces + characters)
        current_char = chr(ord(current_char) + i )

    for i in range(n , 0, -1):
        spaces = ' ' * (n - i)
        characters = ''.join(chr(ord(current_char) + j) for j in range(i * 2 - 1))
        print(spaces + characters)
        current_char = chr(ord(current_char) + i )
        
print_pattern(4)
