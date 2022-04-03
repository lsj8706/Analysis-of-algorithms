import random
import numpy as np
import matplotlib.pyplot as pyplot

# 문제 1
def quickSort(s, low, high):
    if high > low:
        pivot_point = partition(s, low, high)
        quickSort(s, low, pivot_point-1)
        quickSort(s, pivot_point+1, high)

def partition(s, low, high):
    global cnt
    pivot_item = s[low]
    j = low
    for i in range(low+1, high+1):
        cnt += 1
        if s[i] < pivot_item:
            j+=1
            s[i],s[j] = s[j],s[i]
    s[j],s[low] = s[low], s[j]
    return j





x = [100, 200, 300, 400]
y = []
for n in x:
    tot = 0
    for _ in range(100):
        s=[random.randint(0, n) for _ in range(n)]
        cnt = 0
        quickSort(s, 0, n-1)
        tot += cnt
    y.append(tot//100)
print(y)
pyplot.plot(x, y)
pyplot.show()

# 그래프틑 nlog(n)을 따른다.


# 문제 2
def prod2(a, b):
    n = max(len(str(a)), len(str(b)))
    threshold = 2
    if(a==0 or b==0):
        return 0
    elif n <= threshold:
        return a*b
    else:
        m = n//2
        x = a // (10**m)
        y = a % (10**m)
        w = b // (10**m)
        z = b % (10**m)
        i = prod2(x, w)
        j = prod2(x, z)
        k = prod2(w, y)
        l = prod2(y, z)
        return i * (10**(2*m)) + (j+k)*(10**m) + l

a=1234567812345678
b=2345678923456789
print(prod2(a,b))
print(a*b)