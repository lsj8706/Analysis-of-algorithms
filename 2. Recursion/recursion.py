import random
#문제 1
class Data():
    def __init__(self, n, data):
        self.data = data
        self.n = n
        self.cnt = 0
    
    def bs(self, item, low, high):
        if low > high:
            return -1
        else:
            self.cnt += 1
            mid = (low+high)//2
            if item == self.data[mid]:
                return mid
            elif item > self.data[mid]:
                return self.bs(item, mid+1, high)
            else:
                return self.bs(item, low, mid-1)




tot = 0
for i in range(1000):
    l = [random.randint(1, 128) for _ in range(128)]
    data = Data(128, l)
    location = data.bs(random.randint(1,128), 0, 127)
    tot += data.cnt

print(tot//1000)

tot = 0
for i in range(1000):
    l = [random.randint(1, 256) for _ in range(256)]
    data = Data(256, l)
    location = data.bs(random.randint(1,256), 0, 255)
    tot += data.cnt

print(tot//1000)

tot = 0
for i in range(1000):
    l = [random.randint(1, 512) for _ in range(512)]
    data = Data(512, l)
    location = data.bs(random.randint(1,512), 0, 511)
    tot += data.cnt

print(tot//1000)


# 문제 2

def merge_sort(n, s):
    h = n//2
    m = n - h
    if n>1:
        U = s[:h]
        V = s[h:]
        merge_sort(h, U)
        merge_sort(m, V)
        merge(h,m,U,V,s)

def merge(h, m, U, V, s):
    global size
    size += len(U)
    i = j = k = 0
    while i < h and j < m:
        if U[i] < V[j]:
            s[k] = U[i]
            i += 1
        else:
            s[k] = V[j]
            j += 1
        k += 1
    
    if i > h-1:
        for x in range(j, m):
            s[k] = V[x]
            k += 1
    else:
        for y in range(i, h):
            s[k] = U[y]
            k += 1

size = 0
s = [8,3,15,2,9,1,5,7,4,16,10,11,12,13,6,14]
merge_sort(len(s), s)
print(s)
print(size)