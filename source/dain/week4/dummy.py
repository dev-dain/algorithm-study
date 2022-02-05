import copy

a = [[1,2], [3,4]]
b = a[:]
c = copy.deepcopy(a)

# [:]를 하거나 deepcopy를 하거나 id는 달라짐
print(id(a), id(b), id(c))
# 하지만 [:]의 경우 id가 같음
print(id(a[0]), id(b[0]), id(c[0]))
# 재할당의 경우 문제 없음. id가 달라짐
a[0] = [8, 9]
print(*a, id(a[0]))
print(*b, id(b[0]))
# 하지만 리스트 내부 값을 직접 변경할 경우 문제가 생김
# 내부 리스트의 id가 같기 때문이다
a[1].append(10)
print(*a, id(a[1]))
print(*b, id(b[1]))
print(*c)

