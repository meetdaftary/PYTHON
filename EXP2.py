x=input('INPUT HERE:    ')
print("Hello", "World", sep="---",end="  end of print")
a = list()
b = 'Hii'
a.append(b)
print(a)
a = set()
b = 'APPLE'
a.add(b)
print(a)
x = list(map(int, input().split()))
print(x)


colors = ["red", "green", "blue"]
for i, color in enumerate(colors):
    print(f"Index: {i}, Color: {color}")

i = 1
while i <= 10:
    print(i)
    i += 1

i = 10
if i > 15:
 print("10 is less than 15")

number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

coke_price = 1.50
juice_price = 2.00
water_price = 1.00
amount_inserted = float(input("Enter amount inserted (in INR): "))
if amount_inserted >= coke_price:
    print("Enjoy your Coke!")
elif amount_inserted >= juice_price:
    print("Here's your juice!")
elif amount_inserted >= water_price:
    print("Have some refreshing water!")
else:
    print("Insufficient amount. Please insert more money.")

for letter in 'engineers': 
    if letter == 'e' or letter == 's':
        break
print ('Current Letter: ', letter)

for letter in 'engineers': 
    if letter == 'e' or letter == 's':
        continue
print ('Current Letter: ', letter)

for letter in 'engineers': 
    if letter == 'e' or letter == 's':
        pass
print ('Current Letter: ', letter)
