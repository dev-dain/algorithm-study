h, w = map(int, input().split())
heights = list(map(int, input().split()))
result = 0

for i in range(1, w-1):
  left_max = max(heights[:i])
  right_max = max(heights[i+1:])

  height = min(left_max, right_max)
  if heights[i] < height:
    result += height - heights[i]

print(result)

