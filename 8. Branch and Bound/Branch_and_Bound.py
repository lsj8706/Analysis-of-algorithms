import queue

# 1번 문제
class Node:
    def __init__(self,level,weight, profit, include):
        self.level = level
        self.weight = weight
        self.profit = profit
        self.include = include
                
def kp_BFS():
    global maxProfit
    global bestset
    global total_node
    global max_data
    q = queue.Queue()
    temp = n*[0]
    node = Node(-1,0,0,temp)
    q.put(node)
    
    while not q.empty():
        if max_data < q.qsize():
            max_data = q.qsize()
        total_node += 1
        v = q.get()
        level = v.level + 1
        weight = v.weight + w[level]
        profit = v.profit + p[level]
        include = v.include[:]
        u = Node(level,weight,profit,include)
        u.include[u.level] = 1
        if u.weight <= W and u.profit > maxProfit:
            maxProfit = u.profit
            bestset = u.include[:]
        if compBound(u) > maxProfit:
            q.put(u)
        u = Node(level,v.weight,v.profit,v.include)
        if compBound(u) > maxProfit:
            q.put(u)
            
            
def compBound(u):
    if u.weight >= W:
        return 0
    else:
        j = u.level + 1
        bound = u.profit
        totweight = u.weight
        while (j < n and totweight + w[j] <= W):
            totweight += w[j]
            bound += p[j]
            j += 1
        k = j
        if k < n:
            bound += ((W-totweight)*p[k])/w[k]
        return bound
        
        
n=4
W=6
p=[30,28,18,20]
w=[3,4,3,5]
include=[0]*n
maxProfit =0
bestset=n*[0]
total_node = 0
max_data = 0
kp_BFS()
print("1번 문제")
print(bestset)
print("총 노드의 수 : ", total_node)
print("queue에 저장되어 있는 데이터의 쵀대 개수 : ", max_data)



# 2번 문제
class Node:
    def __init__(self,level,weight, profit, bound, include):
            self.level = level
            self.weight = weight
            self.profit = profit
            self.bound = bound
            self.include = include
    def __lt__(self, other):
           return self.bound < other.bound

def kp_Best_FS():
    global maxProfit
    global bestset
    temp = n*[0]
    v = Node(-1,0,0,0.0,temp)
    q = queue.PriorityQueue()
    v.bound = compBound(v)
    q.put((-v.bound,v))
    u = Node(0,0,0,0.0,temp)
    
    while (not q.empty()):
        v = q.get()[1]
        if v.bound > maxProfit:
            level = v.level + 1
            weight = v.weight + w[level]
            profit = v.profit + p[level]
            include = v.include[:]
            u = Node(level, weight, profit, 0.0, include)
            u.include[level] = 1
            if u.weight <= W and u.profit > maxProfit: 
                maxProfit = u.profit
                bestset = u.include
            u.bound = compBound(u)
            if u.bound > maxProfit:
                q.put((-u.bound,u))
            u = Node(level,v.weight, v.profit, 0.0, v.include)
            u.bound = compBound(u)
            if u.bound > maxProfit:
                q.put((-u.bound,u))
        


def compBound(u):
    if u.weight >= W:
        return 0
    else:
        j=u.level+1
        bound = u.profit
        totweight = u.weight
        while j<n and totweight + w[j] <= W:
            totweight += w[j]
            bound += p[j]
            j += 1
        k = j
        if k<n:
            bound += ((W-totweight)*p[k])/w[k]
        return bound




n=4
W=6
p=[30,28,18,20]
w=[3,4,3,5]
include=[0]*n
maxProfit =0
bestset=n*[0]
kp_Best_FS()
print()
print("2번 문제")
print(bestset)
print(maxProfit)

