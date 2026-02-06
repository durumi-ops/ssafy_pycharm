# T = int(input())
# N, M = map(int,input().split())
# #여기까지 입력받기 완료
#
#
# for tc in range(T): #tc 케이스에 대하여
#     arr = [list((input())) for _ in range(N)] #N줄 만큼의 숫자를 입력받는다.
#     print(arr)
#     print(arr[0])
#     print(arr[0][1])
#     print(type(arr[0][1]))
#     print(arr[0][0:3])
#     print(arr[0][0:3][::-1])
#     print(type(arr[0][0:3]))
#     if arr[0][0:3]==arr[0][0:3][::-1]:
#         print(arr[0][0:3]
#     else:
#         print("NO")





    # r, c = 0, 0 # 초기 위치 설정

    #가로열부터 시작
    # for i in range(N):
    #     for j in range(N-M+1):
    #         if arr[i][0][j:j+3] == arr[i][0][j:j+3][::-1]:
    #             print(arr[i][0][j:j+3])
    #         else:
    #             continue

# a=[input()]
# print(a)
# if a[0][1:4] == a[0][1:4][::-1]:
#     print(a[0][1:4])
#     print('OK')
# else:
#     print('FAIL')

T = int(input())
N, M = map(int, input().split())
#여기까지 입력받기 완료


for tc in range(T): #tc 케이스에 대하여
    # arr = [list ((input())) for _ in range(N)] #N줄 만큼의 숫자를 입력받는다.
    # for i in range(N):
    #     for j in range(0,N-M+1):
    #         if arr[i][j:j+3] == arr[i][j:j+3][::-1]:
    #             print(arr[i][j:j+3])
    #         else:
    #             continue
    arr = [list((input())) for _ in range(N)]
    for i in range(N):
        for j in range(0, N - M + 1):
            l = []
            l.append(arr[j][i])
            l.append(arr[j+1][i])
            l.append(arr[j+2][i])
            if l == l[::-1]:
                print(l)
            else: continue