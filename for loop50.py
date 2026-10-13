n = int(input("Enter a number: "))
temp=n
s=0
for i in range(len(str(n))):
    d=n%10
    s=(s*10)+d
    n=n//10
if s==temp:
    print("palindrome number")
else:
    print("not aplindrome number")