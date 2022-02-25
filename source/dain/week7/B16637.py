def calculate(x, y, op):
  return eval(x+op+y)

def dfs(index, val):
  global res
  if index >= N:
    res = max(res, val)
    return

  op = '+' if index == 0 else exp[index-1]
  if (index + 2 < N):
    tmp = calculate(exp[index], exp[index+2], exp[index+1])
    dfs(index + 4, calculate(str(val), str(tmp), op))
  dfs(index + 2, calculate(str(val), str(exp[index]), op))

N = int(input())
exp = list(input())
res = -1e9
dfs(0, 0)
print(res)


# 틀린 코드
# 예제 다 맞는데 22%에서 틀려서 환장할 지경..
'''
from copy import deepcopy

N = int(input())
expression = list(input())
res = int(-1e9)

def calculate(exp):
  length = len(exp)
  if exp[2] == '(':
    res = eval(exp[0] + exp[1] + exp[3])
    idx = 5
  else:
    res = eval(''.join(exp[:3]))
    idx = 3
  while idx < length:
    op = exp[idx]
    if exp[idx+1] == '(':
      n = exp[idx+2]
      idx += 2
    else:
      n = exp[idx+1]
    res = eval(str(res) + op + n)
    idx += 2
  return res

def dfs(exp, index):
  global res
  if (index*2) >= N:
    return
  for i in range(index, N-1):
    new_exp = deepcopy(exp)
    try:
      val = eval(''.join(new_exp[i*2:i*2+3]))
    except:
      return
    new_exp[i*2:i*2+3] = ['(', str(val), ')']
    res = max(res, calculate(new_exp))  
    dfs(new_exp, index+2)
  return

for i in range(0, N//2):
  exp = deepcopy(expression)
  val = eval(''.join(exp[i*2:i*2+3]))
  exp[i*2:i*2+3] = ['(', str(val), ')']
  res = max(res, calculate(exp))
  dfs(exp, i+2)
if N == 1:
  res = ''.join(expression)
print(res)
'''