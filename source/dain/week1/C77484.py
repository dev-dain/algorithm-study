# 01-08 (수정)
# https://programmers.co.kr/learn/courses/30/lessons/77484
def solution(lottos, win_nums):
  lotto = set(sorted(lottos))
  win_num = set(sorted(win_nums))
  match = len(lotto & win_num)
  num = [6, 6, 5, 4, 3, 2, 1]

  if 0 not in lotto:
    return [num[match], num[match]]
  return [num[match + lottos.count(0)], num[match]]
  
print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))