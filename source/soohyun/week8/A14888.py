# 백준 14888 연산자 끼워넣기
# https://www.acmicpc.net/problem/14888

n = int(input()) # 수의 개수
nums = list(map(int, input().split())) # n개의 수
op = list(map(int, input().split())) # 덧셈, 뺄셈, 곱셈, 나눗셈의 개수
ans_max, ans_min = -1e9, 1e9 # 최대값, 최소값

def solve(depth, result, plus, minus, multiply, divide):
	global ans_max, ans_min

	# 모든 숫자를 탐색했다면 최대값, 최소값을 구하고 리턴
	if depth == n:
		ans_max = max(ans_max, result)
		ans_min = min(ans_min, result)
		return

	# 연산자의 개수에 따른 재귀함수 호출
	if plus: 
		solve(depth + 1, result + nums[depth], plus - 1, minus, multiply, divide)
	if minus:
		solve(depth + 1, result - nums[depth], plus, minus - 1, multiply, divide)
	if multiply:
		solve(depth + 1, result * nums[depth], plus, minus, multiply - 1, divide)
	if divide:
		solve(depth + 1, int(result / nums[depth]), plus, minus, multiply, divide - 1)

solve(1, nums[0], op[0], op[1], op[2], op[3])
print(ans_max)
print(ans_min)