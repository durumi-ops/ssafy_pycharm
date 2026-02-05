N = 3

arr = [[0] * N for _ in range(N)]

# 방향, delta리스트 설정
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
# dr / dc 리스트의 인덱스라고 생각하면 됨 (오:0, 아:1, 왼:2. 위:3)


d = 0  # 현재 방향 (오른쪽)
r = 0  # 현재 위치 (row: 행)
c = 0  # 현재 위치 (column: 열)
for num in range(1, N ^ 2 + 1):  # num은 앞으로 1부터 차례대로 채울 '숫자'이다.
    arr[r][c] = num
    nr = r + dr[d]  # 새로운위치(nr) = 현재위치(r)+방향(dr[d])
    nc = c + dc[d]  # 새로운위치(nc) = 현재위치(c)+방향(dr[d])

    if nr < 0 or nr >= N or nc < 0 or nr >= N or arr[nr][nc] != 0:
        d = (d + 1) % 4
        nr = r + dr[d]
        nc = c + dc[d]

    r = nr
    c = nc