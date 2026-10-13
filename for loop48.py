n=int(input("enter any number: "))
s=0
c=n
for i in range(n):
    d=n%10
    s=s+(d*d*d)
    n=n//10
if c==s:
    print("armstrong number")
else:
    print("not armstrong number")