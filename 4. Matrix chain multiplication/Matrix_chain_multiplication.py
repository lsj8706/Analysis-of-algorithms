def printMatrix(d):
    m = len(d)
    n=len(d[0])
    
    for i in range(0,m):
        for j in range(0,n):
            print("%4d" % d[i][j],end=" ")
        print()

def order(p,i,j):
    if i==j:
        print(f'A{i}', end='')
    else:
        k = p[i][j]
        print("(", end='')
        order(p,i,k)
        order(p,k+1,j)
        print(")", end='')

d=[3,5,4,6,7,2,3,4]
n=7

m=[[0 for j in range(1,n+2)] for i in range(1,n+2)]
p=[[0 for j in range(1,n+2)] for i in range(1,n+2)]

for diagonal in range(1, n):
    for i in range(1, n-diagonal+1):
        j = i + diagonal
        min_value = 2147000000
        for k in range(i,j):
            new = m[i][k]+m[k+1][j]+d[i-1]*d[k]*d[j]
            if new < min_value:
                min_value = new
                p[i][j] = k
                m[i][j] = min_value



printMatrix(m)
print()
printMatrix(p)
order(p,1,7)