smallest = int(input("Enter number : "))

for i in range(4):
    n = int(input("Enter another number: "))

    if n < smallest:
        smallest = n

print("smallest number is:", smallest)

