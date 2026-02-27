import sys
from collections import deque

N = int(input())
arr = [list(map(int,input())) for _ in range(N)]

#상하좌우 기준 delta값 설정
dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(y,x):
    # queue는 다음에 방문할 집 목록을 적어두는 메모장
    queue = deque()
    queue.append((y,x)) # 첫번째 집을 우선 메모장에 넣어둔다
    arr[y][x] = 0 #방금 집 확인했으니까 다시 안보게 0으로 만든다.
    count = 1

    while queue: # 메모장에 갈 집이 있을 때까지 시행할건데
        cy, cx = queue.popleft()

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if 0<= nx < N and 0<=ny<N and arr[ny][nx] ==1:
                arr[ny][nx]=0
                queue.append((ny,nx))
                count += 1
    return count

#단지별 집 개수 모아둘 리스트
result = []

for i in range(N):
    for j in range(N):
        if arr[i][j]==1:
            house_count = bfs(i,j)
            result.append(house_count)

result.sort()

print(len(result))
for n in result:
    print(n)

