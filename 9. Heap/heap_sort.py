import math

class Heap(object):
    n = 0
    def __init__(self, data):
        self.data=data
        # heap size를 하나 줄인다
        self.n=len(self.data)-1
        
    def addElt(self,elt):
        self.data.append(elt)
        self.n = len(self.data)-1
        self.siftUp(self.n)

    def siftUp(self, i):
        while(i>=2):
            if (self.data[i] > self.data[math.floor(i/2)]):
                temp = self.data[i]
                self.data[i] = self.data[math.floor(i/2)]
                self.data[math.floor(i/2)] = temp
            i = math.floor(i/2)
            
    def siftDown(self,i):
        siftkey = self.data[i]
        parent = i
        spotfound = False

        while(2*parent <= self.n and not spotfound):
            if (2*parent < self.n and self.data[2*parent] < self.data[2*parent+1]):
                largerchild = 2*parent +1
            else:
                largerchild = 2*parent
            if (siftkey < self.data[largerchild]):
                self.data[parent] = self.data[largerchild]
                parent = largerchild
            else:
                spotfound = True
        self.data[parent] = siftkey

    # 방법 1
    # 데이터가 입력되는 순서대로 heap을 재구성 => h라는 임시 힙을 만들고
    # addElt를 통해 데이터를 한개씩 추가 + heap 재구성
    def makeHeap1(self):
        temp = [0]
        h = Heap(temp)
        for i in self.data:
            h.addElt(i)
        self.data = h.data

    # 방법 2
    # 모든 데이터를 트리에 넣은 상태에서 heap 구성 (효율적)
    def makeHeap2(self):  
        for i in range(self.n//2,0,-1):
            self.siftDown(i)

    def root(self):
        keyout = self.data[1]
        self.data[1] = self.data[self.n]
        self.n -= 1
        # Heap이 더 이상 없을 때에는 down 없음
        if(self.n>0):
            self.siftDown(1)
        return keyout
    
    def removeKeys(self):
        s = []
        for _ in range(self.n,1,-1):
            a = self.root()
            s.append(a)
        return s

def heapSort1(a):
    a = Heap(a)
    a.makeHeap1()
    s = a.removeKeys()
    return s

def heapSort(a):
    a = Heap(a)
    a.makeHeap2()
    s = a.removeKeys()
    return s


# 1번 문제
# 인덱스를 간단히 하기 위해 처음 엘리먼트 0 추가
print("1번 문제")    
a=[0,11,14,2,7,6,3,9,5]
b=Heap(a)
b.makeHeap1()
print(b.data)
s=heapSort1(a)
print(s)
print()



# 2번 문제
# 인덱스를 간단히 하기 위해 처음 엘리먼트 0 추가
print("2번 문제")    
a=[0,11,14,2,7,6,3,9,5]
b=Heap(a)
b.makeHeap2()
print(b.data)
b.addElt(50)
print(b.data)
s=heapSort(a)
print(s)
print()
