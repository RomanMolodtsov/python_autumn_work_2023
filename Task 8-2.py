lst = [[1,5,3], [2,44,1,4], [3,3]]
# def f(n):
#     return len(n)
print(sorted(lst, key = lambda x: (len(x), x.sort())))