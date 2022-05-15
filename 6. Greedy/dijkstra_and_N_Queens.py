# 1번 문제
inf = 100000000
w = [[0,15,4,11,5],[inf,0,inf,1,inf],
   [inf,4,0,2,inf], [inf,inf,inf,0,inf], [inf,3,inf,1,0]]
n = 5
f = set()
touch = n*[0] # 마지막으로 거쳐가는 노드
length = n*[0] # 최단 거리
visited = n*[0] # 방문한 노드
NoC = 0

for i in range(1, n):
    length[i] = w[0][i]

# 가장 최소 거리를 가지는 노드 반환
def get_small_length_node():
    min_value = inf
    index = 0
    for j in range(1,n) :
        if (length[j] < min_value) and visited[j] == 0:
            min_value = length[j]
            index = j
    return index

# dijkstra
for i in range(n-1) :
    vnear = get_small_length_node()
    visited[vnear] = 1
    e = (touch[vnear], vnear)
    f.add(e)

    for j in range(1, n) :
        if (length[vnear] + w[vnear][j] < length[j]) :
            length[j] = length[vnear] + w[vnear][j]
            NoC += 1
            touch[j] = vnear

print("1번 문제")
print(f)
print(length)
print(NoC)
print()


# 2번 문제
result_count = 0 # 해의 총 개수
node_count = 0 # 생성한 상태 공간 트리의 총 노드 수

def promising(i, col):
    k = 0 
    switch = True
    while (k < i and switch == True):
        # col[i] == col[k]는 같은 열인지 확인, abs(col[i]-col[k]) == i-k는 같은 대각선인지 확인
        if (col[i] == col[k] or abs(col[i]-col[k]) == i-k):
            switch = False
        k += 1
    return switch

def queens(n, i, col):
    global result_count, node_count
    if promising(i, col):
        if (i == n-1):
            #print(col)
            result_count += 1
        else :
            for j in range(0,n):
                col[i+1] = j
                node_count += 1
                queens(n, i+1, col)          

n = 7
col = n*[0]
queens(n, -1, col)
print("2번 문제") 
print("해의 총 개수", result_count)
print("생성한 상태 공간트리의 총 노드 수", node_count)
