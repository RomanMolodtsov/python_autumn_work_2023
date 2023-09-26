str1 = input('Введите первое предложение: ').lower()
str2 = input('Введите второе предложение: ').lower()

s1 = list(str1)
s2 = list(str2)

s1.sort()
s2.sort()

print(s1 == s2)
