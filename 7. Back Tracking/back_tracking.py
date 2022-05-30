# 1번 문제
def promising(i, weight, total):
    return (weight+total>=W) and (weight==W or weight+w[i]<=W)

def s_s(i, weight, total, include):
    global cnt
    if promising(i+1, weight, total):
        if weight==W:
            print("해", include)
        else:
            cnt += 2
            include[i+1] = 1
            s_s(i+1, weight+w[i+1], total-w[i+1], include)
            include[i+1] = 0
            s_s(i+1, weight, total-w[i+1], include)
    

n = 5
w = [1,2,3,4,15]
W = 15
print("1번 문제")
print("items =",w, "W =", W)
include = n*[0]
total = 0
for k in w:
    total+=k

cnt = 0 # 총 노드의 수
s_s(-1,0,total,include)
print("총 노드의 수: ", cnt)


# 2번 문제
def color(i, vcolor):
    global cnt
    if promising(i, vcolor):
        if i+1==n:
            print("해", vcolor)
        else:
            for color_num in range(1, m+1):
                vcolor[i+1] = color_num
                cnt += 1
                color(i+1, vcolor)
    

def promising(i, vcolor):
    for j in range(0, i):
        if (W[i][j] and vcolor[i]==vcolor[j]):
            return False
    return True


n=5
W=[[0,1,1,0,1],[1,0,1,1,0],[1,1,0,1,0],[0,1,1,0,1],[1,0,0,1,0]]
vcolor=n*[0]
m=3
cnt = 0
print()
print("2번 문제")
color(-1,vcolor)
print("총 노드의 수: ", cnt)