s = input()
bomb = input()
# 시간초과
# while True:
#   idx = s.find(bomb)
#   if idx == -1:
#     break
#   s = s.replace(bomb, '')
# print(s if s else 'FRULA')

# 폭발 문자열의 마지막부터 검사를 해야 스택처럼 구현 가능
stack = []
for c in s:
  stack.append(c)
  if c == bomb[-1] and ''.join(stack[-len(bomb):]) == bomb:
    del stack[-len(bomb):]

print(''.join(stack) if ''.join(stack) else 'FRULA')
