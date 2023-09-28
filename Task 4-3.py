s1 = input()
s2 = input()
ab ='qwertyuiopasdfghjklzxcvbnm'
ds1 = {}
ds2 = {}
for i in s1.lower():
    if i in ab:
        ds1[i] = ds1.get(i, 0) + 1
for i in s2.lower():
    if i in ab:
        ds1[i] = ds2.get(i, 0) + 1
print(ds1 == ds2)

