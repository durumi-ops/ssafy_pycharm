T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # 입력받기 완료

    #상하좌우 delta list
    # dy = [-1,1,0,0]
    # dx = [0,0,-1,1]

    def cal(y,x):
        list =[arr[y][x]]
        for num in range(4):
            dy = [-1, 1, 0, 0]
            dx = [0, 0, -1, 1]
            new_y = y + dy[num]
            new_x = x + dx[num]
            if new_y > (N - 1) or new_y < 0 or new_x > (N - 1) or new_x < 0:
                continue

            list.append((arr[new_y][new_x]))

        return(sum(list))

    total = 0
    max_y = 0
    max_x = 0

    for i in range(N):
        st_y = i
        for j in range(N):
            st_x = j
            cal(st_y,st_x)
            if cal(st_y,st_x) > total:
                total = cal(st_y,st_x)
                max_y = st_y
                max_x = st_x

    print(f'#{tc} {total} {max_y} {max_x}')






    #         if cal(st_y, st_x) > total:
    #             total = cal(st_y, st_x)
    #             max_y = st_y
    #             max_x = st_x
    #
    # print(total, max_y, max_x)



    # for i in range(N):
    #     for j in range(N):
    #         print(cal(i,j))


    # now_y = 0
    # now_x = 0
    # for i in range(N):
    #     for j in range(N):
    #         now_y += i
    #         now_x += j




        #     for num in range(4):
        #         dy = [-1, 1, 0, 0]
        #         dx = [0, 0, -1, 1]
        #         now_y += dy[num]
        #         now_x += dx[num]
        #         if now_y > N - 1 or now_y < 0 or now_x > N - 1 or now_x < 0:
        #             continue
        #         list.append((arr[now_y][now_x]))
        #
        # print(list)

        # print(list)


    # print(list)            # total = sum(list)

# dy = [-1,1,0,0]
# dx = [0,0,-1,1]
#
# now_y = 2
# now_x = 2
#
# # print(arr[now_y][now_x])
# list=[]
# for i in range(4):
#     now_y = 2
#     now_x = 4
#     now_y += dy[i]
#     now_x += dx[i]
#     if now_y > N-1 or now_y <0 or now_x > N-1 or now_x < 0:
#         continue
#     list.append(arr[now_y][now_x])

# -------------------강사님ver.-------------------------
# import sys
# sys.stdin = open("input.txt", "r")
#
# # 상하좌우 델타
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     max_y, max_x, max_total = 0, 0, 0
#
#     # sy, sx : 파리채를 치는 지점
#     for sy in range(N):
#         for sx in range(N):
#             # (sy, sx) + 상하좌우 값 -> 더한다.
#             total = arr[sy][sx]
#
#             for i in range(4):
#                 new_y = sy + dy[i]
#                 new_x = sx + dx[i]
#
#                 # 해당 방향의 좌표가 범위를 벗어나면 continue
#                 if new_y < 0 or new_y >= N or new_x < 0 or new_x >= N:
#                     continue
#
#                 total += arr[new_y][new_x]
#
#             # 최대값 갱신
#             if total > max_total:
#                 max_y = sy
#                 max_x = sx
#                 max_total = total
#
#     print(f"#{tc} {max_total} {max_y} {max_x}")