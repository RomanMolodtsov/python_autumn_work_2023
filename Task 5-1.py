n = int(input())
lst = [0, 1, 0]
print(1)
for i in range(2, n+1):
    x = lst[0]
    for j in range(1, i+1):
        y = x + lst[j]
        print(y, end = ' ')
        x = lst[j]
        lst[j] = y
    print()
    lst.append(0)

