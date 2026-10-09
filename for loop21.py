'''largest = 0
for i in range(5):
    n = int(input("Enter a number: "))

    if n > largest:
        largest = n

print("Largest number:", largest)'''



largest = int(input("Enter number 1: "))

for i in range(4):
    n = int(input("Enter another number: "))

    if n > largest:
        largest = n

print("Largest number is:", largest)