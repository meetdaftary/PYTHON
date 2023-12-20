# n = int(input("Enter the count of numbers: "))

# print("Enter", n, "numbers:")

# with open("T1.txt", "w") as f:
#     for i in range(n - 1):
#         f.write(str(input()) + "\n")
#     f.write(str(input()))

# with open("T1.txt", "r") as f1, open("T2.txt", "w") as f2:
#     l = []
#     for line in f1:
#         l.append(int(line))
#     l.sort()
#     for i in range(n):
#         f2.write(str(l[i]) + "\n")
    



# file_read = open("T1.txt", "r")
# List = list()

# with file_read:
#     # Read the file contents
#     f = file_read.read()
#     # Split the contents into words
#     f = f.split()
#     # Append each word to the List
#     for line in f:
#         List.append(str(line)[::-1])

# # Sort the list by word length and then alphabetically
# List.sort(key=lambda item: (item, len(item)))

# print("List of sorted words is:")
# for word in List:
#     print(word)

# # Open and write to the output file
# file_write = open("T2.txt", "w")
# for word in List:
#     file_write.write(word + "\n")

# file_write.close()




