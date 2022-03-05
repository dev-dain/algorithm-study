import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int,input().split())
arr = deque(list(map(int,input().split())))

ans = 1 # 1번째 단계부터 시작

robot = deque(list([0]*n))

while True:
    # 1단계 벨트가 한 칸 회전한다.
    arr.rotate(1)
    robot.rotate(1)
    robot[-1] = 0

    for i in range(-2, -n-1, -1):
        # 내구도가 1이상이고 이동하려는 칸에 로봇이 없다면 이동
        if robot[i] == 1 and robot[i+1] == 0 and arr[i+1-n] > 0:
            robot[i] = 0
            robot[i+1] = 1
            arr[i+1-n] -= 1
    robot[-1] = 0
    
    # 올리는 위치가 0이 아니라면 로봇을 올림
    if robot[0] == 0 and arr[0] > 0:
        robot[0] = 1 
        arr[0] -= 1
        
    # 0인 칸이 k개 이상일 경우 종료
    if arr.count(0) >= k:
        break
    ans += 1
    

print(ans)