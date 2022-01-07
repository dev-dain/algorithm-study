# 01-07
s = input()
stack = []
tmp = 1
res = 0
# for c in s를 하면 안 되고 길이로 돌아야 함
for i in range(len(s)):
  if s[i] == '(':
    tmp *= 2
    stack.append(s[i])
  elif s[i] == '[':
    tmp *= 3
    stack.append(s[i])

  elif s[i] == ')':
    if not stack or stack[-1] == '[':
      res = 0
      break
    if s[i-1] == '(':
      res += tmp
    tmp //= 2
    stack.pop() # pop도 까먹지 말고 꼭
  
  else:
    if not stack or stack[-1] == '(':
      res = 0
      break
    # [()]의 경우 ] 직전 문자가 )이므로 더하지 않고 넘어감
    # 단, 이 경우는 오류는 아님
    if s[i-1] == '[':
      res += tmp
    tmp //= 3
    stack.pop() # pop 까먹지 말기

if stack:
  res = 0
print(res)