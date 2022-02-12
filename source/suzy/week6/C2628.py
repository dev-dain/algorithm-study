x, y= map(int, input().split())
x_list = [0,x]
y_list = [0,y]
for _ in range(int(input())):
    xy, cut = map(int, input().split())
    if xy == 0:
        y_list.append(cut)
    else:
        x_list.append(cut)
        
# 좌, 위 대조를 위해    
x_list.sort()
y_list.sort()

max_area = 0
for i in range(1, len(x_list)):
    for j in range(1, len(y_list)):
        width = x_list[i] - x_list[i-1]
        height = y_list[j] - y_list[j-1]
        max_area = max(max_area, width * height)
print(max_area)