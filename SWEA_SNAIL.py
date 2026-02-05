T = int(input())
N_list = [int(input()) for _ in range(T)]
for tc in range(1,T+1):
    N = N_list[tc-1]
    print(f'#{tc}')
    arr = [[0] * N for _ in range(N)] # 0으로 이루어진 임시 배열을 만들어둔다.

    #오른쪽-아래-왼쪽-위 순서대로 delta 리스트를 만들어둔다.
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    r, c = 0, 0 #처음 시작 위치
    d = 0 #처음 방향 (d=0:오른쪽, d=1:아래, d=2:위, d=3: 왼쪽)

    for num in range(1, N*N + 1):
        #1부터 N*N까지 숫자를 num에 넣을 것임
        arr[r][c] = num
        #arr[0][0] = 1부터 시작

        nr = r + dr[d]
        #디음번의 '열' 위치
        nc = c + dc[d]
        #다음번의 '행' 위치
        if nr < 0 or nr >= N or nc < 0 or nc >= N or arr[nr][nc] != 0:
            #위치 인덱스가 0보다 작거나, N보다 크거나 같다면(모서리에 위치할 때), 또는 해당 다음 위치에 0이 들어있지 않다면,
            d = (d + 1) % 4

            nr = r + dr[d]
            nc = c + dc[d]

        r, c = nr, nc #위치 갱신


    for row in arr:
        print(*row) #리스트 앞에 *을 붙이면 자동으로 공백을 사이에 두고 안에 있는걸 꺼내서 출력한다.
