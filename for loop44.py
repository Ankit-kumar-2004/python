count=0
for i in range(2,101):
    c=0
    for j in range(2,i):
        if i%j==0:
            c+=1
    if c==0:
        count+=1
print(count)