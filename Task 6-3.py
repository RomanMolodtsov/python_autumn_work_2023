str = set(input('Введите строку: '))
alf = 'qwertyuiopasdfghjklzxcvbnm'
numbers = '1234567890'
words = ''
num = ''
another = ''
for i in str:
    if i in numbers:
        num += i
    elif i in alf:
        words += i
    else:
        another += i
print(words, num, another)