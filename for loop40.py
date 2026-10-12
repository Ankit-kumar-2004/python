n=[10,20,10,20,30,40]
for i in range(len(n)):
    for j in range(i+1,len(n)):
        if n[i]==n[j]:
            print(n[i])
            break