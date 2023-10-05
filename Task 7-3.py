lst = [[1,1], [2,2], [3,4,5,6], [23, 3, 6]]
cmn = []
for i in lst:
    cmn.extend(i)
print(sorted(cmn)[-3:])