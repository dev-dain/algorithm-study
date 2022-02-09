s = input()
t = input()
visited = set()
flag = False

def dfs(string):
  global flag
  if flag:
    return

  if len(string) < len(s):
    return

  if string not in visited:
    visited.add(string)
    if string == s:
      flag = True
      return
    if string[0] == 'B':
      dfs(''.join(list(string[1:])[::-1]))
    if string[-1] == 'A':
      dfs(''.join(list(string[:-1])))
  
dfs(t)
print(1 if flag else 0)