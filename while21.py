n=121
c=n
s=0
while n>0:
    d=n%10
    s=(s*10)+d
    n=n//10
if c==s:
    print("palindrome")
else:
    print("not palindrome")