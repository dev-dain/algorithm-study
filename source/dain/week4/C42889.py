def solution(N, stages):
  l = []
  player_cnt = len(stages)
  not_clear = [0] * (N+2)
  players = [0] * (N+2)
  for i in range(player_cnt):
    not_clear[stages[i]] += 1
  for i in range(1, len(not_clear)):
    players[i] = player_cnt - sum(not_clear[:i])

  # filter를 매번 사용하면 시간초과가 걸릴 수밖에 없다
  # 그러니 미리 구해주는 것이 더 현명하다
  for i in range(1, N+1):
    try:
      percent = not_clear[i] / players[i]
    except:
      percent = 0
    l.append((i, percent))
  l.sort(key=lambda x: -x[1])
  return [x[0] for x in l]
  

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))
