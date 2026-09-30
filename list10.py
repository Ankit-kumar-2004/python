number=[1,2,2,3,4,4,5,5]
result=[]
for num in number:
    if num not in result:
        result.append(num)
print(result)