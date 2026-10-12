n=[10,20,10,20,30,40]
unique=[]
for i in n:
    if i not in unique:
        unique.append(i)
print(unique)