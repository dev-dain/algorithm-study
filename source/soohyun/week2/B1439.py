S = input()
num = '' # 탐색하고 있던 숫자
zero, one = 0, 0

for s in S:
    if s != num: # 현재 숫자와 탐색하고 있던 숫자가 달라지면 개수에 +1, 탐색하고 있던 숫자를 변경
        if s == '0':
            zero += 1
        else:
            one += 1
        num = s
print(min(zero, one))