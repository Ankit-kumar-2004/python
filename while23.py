i = 2
n = 5
c = 0

while i < n:
    if n % i == 0:
        c += 1
    i += 1

if c == 0:
    print("prime number")
else:
    print("not prime number")