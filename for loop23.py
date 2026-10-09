positive=0
negative=0
for i in range(5):
    n=int(input("enter number"))
    if n>0:
        positive+=1
    elif n<0:
        negative+=1
print(positive)
print(negative)