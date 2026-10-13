for i in range(1, 1001):
    temp = i
    digits = len(str(i))
    total = 0

    for j in range(digits):
        digit = temp % 10
        total += digit ** digits
        temp = temp // 10

    if total == i:
        print(i, end=" ")