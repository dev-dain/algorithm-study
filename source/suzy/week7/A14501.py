import sys
input = sys.stdin.readline

N = int(input())

schedule = [list(map(int, input().split())) for _ in range(N)]

answer = 0
def earn(day, money):
    global answer
    answer = max(answer, money)

    if day >= N:
        return

    if day + schedule[day][0] <= N:
        earn(day + schedule[day][0], money + schedule[day][1])
        earn(day + 1, money)
    else:
        earn(day + 1, money)
    return

earn(0, 0)
print(answer)