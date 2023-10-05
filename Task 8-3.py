lst = ['abab', 'xx', 'aaaaaa', 'abcbab']
print(sorted(lst, key=lambda x: (-len(set(x)), x[0])))