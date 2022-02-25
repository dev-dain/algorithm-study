def solution(word):
  flag = False
  start_dict = {'A': 0, 'E': 781, 'I': 1562, 'O': 2343, 'U': 3124}
  (flag, res) = dfs(word, word[0], '', start_dict[word[0]], flag)
  return res
  
def dfs(word, add, tmp, count, flag):
  if flag or len(tmp) == 5:
    return (flag, count)
  if word == tmp:
    flag = True
    return (flag, count)

  tmp += add
  count += 1

  if not flag:
    flag, count = dfs(word, 'A', tmp, count, flag)
  if not flag:
    flag, count = dfs(word, 'E', tmp, count, flag)
  if not flag:
    flag, count = dfs(word, 'I', tmp, count, flag)
  if not flag:
    flag, count = dfs(word, 'O', tmp, count, flag)
  if not flag:
    flag, count = dfs(word, 'U', tmp, count, flag)
  return (flag, count)
  
print(solution('AAAAE'))
print(solution('AAAE'))
print(solution('I'))
print(solution('EIO'))
