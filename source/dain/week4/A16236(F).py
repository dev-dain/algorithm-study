N = int(input())
sea = []
location = []
fish = []
for i in range(N):
  sea.append(list(map(int, input().split())))
  for j in range(N):
    if sea[i][j] == 9:
      location = [i, j]
    if sea[i][j] in (1, 2, 3, 4, 5, 6):
      fish.append([sea[i][j], [i, j]])
fish.sort(key=lambda x: (x[0]))
print(fish)
scale = 2
cnt = 0
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
sec = 0

while True:
  if not fish:
    break
  if len(fish) == 1:
    if fish[0][0] >= scale:
      print(fish)
      break

    tx, ty = fish[0][1]
    sec += 1
    if [tx, ty] == location:
      sea[tx][ty] = 0
      cnt += 1
      fish.pop()
    
    else:
      if tx > location[0]:
        location[0] += 1
        continue
      elif tx < location[0]:
        location[0] -= 1
        continue
      elif ty > location[1]:
        location[1] += 1
        continue
      else:
        location[1] -= 1
        continue
  # 거리가 제일 가까운 걸 어떻게 찾아야?
  # 먹을 수 있는 물고기가 여러 마리인 경우
  else:
    for i in range(4):
      tx = location[0] + dx[i]
      ty = location[1] + dy[i]
      if tx < 0 or tx >= N or ty < 0 or ty >= N:
        continue
      if sea[tx][ty] < scale:
        location = tx, ty
        sec += 1
        cnt += 1
        continue
    
  if cnt == scale:
    scale += 1
    cnt = 0

      
    
print(sec)