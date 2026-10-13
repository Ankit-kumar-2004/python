n=5
c=0
for i in range(1,6):
    if n%i==0:
        c+=1
if c==2:
    print("primer number")
else:
    print("not prime number")