st = str(input('Введите предложение:'))
lst = st.split()
m = max(lst, key=len)
for i in lst:
    if len(i) == len(m):
        print(i)
