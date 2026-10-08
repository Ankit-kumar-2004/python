n=153
c=n
s=0
while n>0:
    d=n%10
    s=s+(d*d*d)
    n=n//10
if c==s:
    print("Armstrong number")
else:
    print("not armstrong number")