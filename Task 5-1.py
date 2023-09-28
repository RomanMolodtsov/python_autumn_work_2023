n = int(input("Введите число строк: "))
for i in range(n):
    print(' '.join(map(str, str(11 ** i))))
