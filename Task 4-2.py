n = int(input('Введите число: '))
mat = [[0]*n for i in range(n)]
st, m = 1, 0
mat[n//2][n//2] = n*n
for i in range(n//2):
    for j in range(n-m):
        mat[i][j+i] = st
        st += 1
    for j in range(i+1, n-i):
        mat[j][-i-1] = st
        st += 1
    for j in range(i + 1, n - i):
        mat[-i - 1][-j - 1] = st
        st += 1
    for j in range(i + 1, n - (i + 1)):
        mat[-j - 1][i] = st
        st += 1
    m += 2
for i in mat:
    print(*i)