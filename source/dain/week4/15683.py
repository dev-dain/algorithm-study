import copy

n, m = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(n)]
cam = []
# 동남서북 방향
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
  for j in range(m):
    if office[i][j] in (1, 2, 3, 4, 5):
      # 카메라 모드 번호, 좌표가 들어감
      cam.append((office[i][j], i, j))

mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]],
]
result = n * m

def fill(office, d, x, y):
  for i in d:
    nx = x
    ny = y
    while True:
      nx += dx[i]
      ny += dy[i]
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        break
      if office[nx][ny] == 6:
        break
      elif office[nx][ny] == 0:
        office[nx][ny] = -1

# depth는 몇 단계까지 짚어 내려왔는지를 알림
def dfs(depth, office):
  global result

  # 여기서 잡았다는 건 1가지 경우의 수를 완료했다는 것
  # 즉, 이 if문은 모든 경우의 수만큼 걸림
  if depth == len(cam):
    count = 0
    for i in range(n):
      count += office[i].count(0)
    # 사각지대가 더 작아졌다면 갱신
    result = min(result, count)
    return

  # temp = office[:]는 잘못된 결과가 나옴
  # copy.deepcopy와 [:] 차이를 알아둡시다
  # temp = office[:]
  temp = copy.deepcopy(office)
  # 현재 depth의 카메라 모드 번호와 좌표
  cam_num, x, y = cam[depth]

  for i in mode[cam_num]:
    # 일단 이 카메라 모드가 감시할 수 있는 방향으로 테스트
    fill(temp, i, x, y)
    # 다음 카메라로 넘어가면서 DFS
    dfs(depth+1, temp)
    # for문 다시 돌아서 fill 함수 해야되니까 temp를 다시 원상복구시킴
    # temp = office[:]
    temp = copy.deepcopy(office)

dfs(0, office)
print(result)