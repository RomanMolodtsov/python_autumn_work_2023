n = int(input("Введите число: "))
st = str(n)
lst = list(st)
k = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in lst:
    if i == '0': k[0] += 1
    if i == '1': k[1] += 1
    if i == '2': k[2] += 1
    if i == '3': k[3] += 1
    if i == '4': k[4] += 1
    if i == '5': k[5] += 1
    if i == '6': k[6] += 1
    if i == '7': k[7] += 1
    if i == '8': k[8] += 1
    if i == '9': k[9] += 1
a=0
for i in k:
    print(a, '-', i)
    a+=1

