# lst = [234, 2, 54, 645, 23, 75, 1, 75, 43, 8789, 5]
# a = lst[0]
# for i in lst:
#     for j in range(0, len(lst)-1):
#         if lst[j] < a:
#             a = int(lst[j])
# print(a)

lst=[234, 2, 54, 645, 23, 75, 1, -75, 43, 8789, 5]
а = lst[0]
for i in lst:
    if i <а: а = i
print(а)