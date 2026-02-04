N=int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

dy = [-1,1,0,0]
dx = [0,0,-1,1]

now_y = 2
now_x = 2

# print(arr[now_y][now_x])
list=[]
for i in range(4):
    now_y = 2
    now_x = 4
    now_y += dy[i]
    now_x += dx[i]
    if now_y > N-1 or now_y <0 or now_x > N-1 or now_x < 0:
        continue
    list.append(arr[now_y][now_x])
print(list)

