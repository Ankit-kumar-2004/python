text=input("enter a string")
c=0
for i in text:
    if i.isalpha() and i.lower() not in "aeiou":
        c+=1
print(c)