import math
print(math.sin(60))
print(math.pi)


animals = ['lion', 'zebra', 'elephant']
animals.append('tiger')
print(animals)
x = animals.copy()
print(x)
print(animals.count('lion'))
animals2 = ['bear', 'wolf', 'fox']
animals.extend(animals2)
print(animals)
print(animals.index('zebra'))
animals.insert(3, 'monkey')
print(animals)
animals.pop(2)
print(animals)
animals.remove('lion')
print(animals)
animals.reverse()
print(animals)
animals.sort()
print(animals)
animals.clear()
print(animals)


t = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(t.count(7))
print(t.index(8))


vehicles={"sedan","coupe","hatchback"}
vehicles.add("truck")
print(vehicles)
x=vehicles.copy()
countries={"france","germany","italy"}
z=x.difference(countries)
vehicles.discard("coupe")
z=x.intersection(countries)
z=x.union(countries)
vehicles.pop()
vehicles.clear()
print(vehicles)


d = {
 "brand": "Audi",
 "model": "A8",
 "year": 2000
}
x = d.copy()
print(x)
x = d.keys()
print(x)
d.pop('model')
print(d)
x = d.get('brand')
print(x)
x = d.values()
print(x)
x = d.items()
print(x)
d.clear()
print(d)



def histogram(l):
    """
    Returns a list of pairs (number, repetitions) sorted by repetitions and then by number.
    Args:
        l: A list of integers.
    Returns:
        A list of pairs (number, repetitions) sorted as described.
    """
    count = 0
    x = []
    k = []
    for i in range(len(l)):
        index = i
        count = 0
        # Nested loop to count repetitions of the current element
        for j in range(index, len(l)):
            if l[index] == l[j] and l[index] not in k:
                count += 1
                k.append(l[index])
        # Add element and its count to the output list if non-zero
        if count != 0:
            x.append((l[index], count))
    # Sort the list by repetitions and then by number
    x.sort(key=lambda item: (item[1], item[0]))
    return x
# Example usage
print("Enter the numbers:")
data = list(map(int, input().split()))
result = histogram(data)
print(f"Histogram of data: {result}")


def is_perfect(num):
  """
  Checks if a number is a perfect number (sum of its divisors excluding itself equals the number).
  Args:
    num: The number to be checked.
  Returns:
    True if the number is perfect, False otherwise.
  """
  sum_of_divisors = 0
  for i in range(1, num):
    if num % i == 0:
      sum_of_divisors += i
  return sum_of_divisors == num
# Example usage
number = int(input("Enter a number: "))
if is_perfect(number):
  print(f"{number} is a perfect number.")
else:
  print(f"{number} is not a perfect number.")


def hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from peg {source} to peg {target}")
        return
    hanoi(n - 1, source, target, auxiliary)
    print(f"Move disk {n} from peg {source} to peg {target}")
    hanoi(n - 1, auxiliary, source, target)
disks = int(input("Enter the number of disks: "))
hanoi(disks, 'A', 'B', 'C')


