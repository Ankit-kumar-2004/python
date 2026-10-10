text=input("enter string")
c=0
for i in text:
    if i.lower() in "aeiou":
        c+=1
print(c)        