import sys
sys.stdin = open('input.txt','r')

T = int(input())
dy = [-1,1,0,0]                     # 상-하-좌-우 순서
dx = [0,0,-1,1]

for tc in range(1,T+1):
    N = int(input())                # N 배열을 입력받는다.
    arr = [list(map(int,input().split())) for _ in range(N)]

    # 초기 위치 세팅
    # r = 0
    # c = 0
    cnt = 0 # 카운팅 초기값 세팅 = 0 으로 시작
    for y in range(N):
        for x in range(N):
            new_y = y
            new_x = x
            sub_list = []
            for i in range(4):
                new_y += dy[i]
                new_x += dx[i]
                if new_y < 0 or new_x <0 or new_x > N-1 or new_y > N-1:
                    continue
                if arr[new_y][new_x] < arr[y][x]:
                    sub_list.append(arr[new_y][new_x])



