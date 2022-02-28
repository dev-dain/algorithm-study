import sys
input = sys.stdin.readline

n = int(input())
name = [input().rstrip() for _ in range(n)]

increasing = sorted(name)
decreasing = sorted(name, reverse=True)

if name == increasing:
    print("INCREASING")
elif name == decreasing:
    print("DECREASING")
else:
    print("NEITHER")