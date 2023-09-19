x = int(input("Введите первое число: "))
y = int(input("Введите второе число(кроме нуля): "))
if y==0:
    print("Не балуйся!")
else:
    a = x+y
    b = x-y
    c = x*y
    d = x/y
    e = x//y
    new_list =[a, b, c, d, e]
    print(max(new_list))

