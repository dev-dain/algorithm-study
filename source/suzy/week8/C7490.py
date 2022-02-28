import copy

def recurcive(array, n):
    if len(array) == n:
        operators_list.append(copy.deepcopy(array))
        # 재귀로 append 할 때 deepcopy
        return

    array.append(' ')
    recurcive(array, n)
    array.pop()

    array.append('+')
    recurcive(array, n)
    array.pop()

    array.append('-')
    recurcive(array, n)
    array.pop()

t = int(input()) # 테스트케이스 횟수
for _ in range(t):
    n = int(input())
    operators_list = []
    recurcive([], n - 1)
    integer = [i for i in range(1, n+1)]

    for operator in operators_list:
        string = ""
        for i in range(n-1):
            string += str(integer[i]) + operator[i]
        string += str(integer[-1])
        if eval(string.replace(" ", "")) == 0:
            print(string)
    print()