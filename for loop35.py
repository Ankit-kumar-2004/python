text = input("Enter a string: ")
reverse = ""

for i in range(len(text) - 1, -1, -1):
    reverse += text[i]
if text == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")
