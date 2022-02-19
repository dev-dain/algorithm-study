import sys
input = sys.stdin.readline

n = 10
graph = [list(map(int, input().split())) for _ in range(n)]
papers = [0,5,5,5,5,5] # 각 색종이 개수

# 색종이를 붙일 수 있는지 확인
def checkarr(x,y,size):
    for i in range(x,x+size):
        for j in range(y,y+size):
            if 0<=i<n and 0<=j<n and graph[i][j] == 1:
                pass
            else:
                return False
    return True

# 색종이를 붙이거나 떼기
def updatepaper(x,y,size,method):
    # 붙였을 경우 0으로 떼는 경우 1로
    for i in range(x, x+size):
        for j in range(y, y+size):
            graph[i][j] =  method
            
result = 25
# 완전탐색 dfs
def dfs(cnt):
    global result
    
    if cnt > result:
        return
    
    F = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                x,y = i,j
                F = 1
                break
        if F ==1 :
            break
        
    # 1이 더이상 없을 경우
    if F == 0:
        if cnt < result:
            result = cnt
        return
    
    for size in range(5,0,-1): # 5부터 1까지 색종이 size
        if papers[size]>0 and checkarr(x,y,size):
            updatepaper(x,y,size,0)
            papers[size] -= 1
            dfs(cnt+1)
            updatepaper(x,y,size,1)
            papers[size] += 1

dfs(0)
if result == 25:
    print(-1)
else:
    print(result)