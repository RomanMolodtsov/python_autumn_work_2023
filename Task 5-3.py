fib1 = fib2 = 1
n = int(input('Введите число: '))
if n ==1:
    print('1')
elif n == 2:
    print('1 1')
else:
    print(fib1, fib2, end=' ')
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=' ')