T = int(input())
for tc in range(1,T+1):
    N = int(input()) #고객 수를 입력받는다.
    customers = list(map(int,input().split())) #고객에게 부과된 기본요금 리스트 입력받는다.
    P = int(input()) # 요청의 개수 P를 입력받는다.
    require = [list(map(int,input().split())) for _ in range(P)] #P번만큼 반복하여 요청사항을 입력받는다.
    # 여기까지 입력받기 완료

    delta = [0]*(N+1) #마지막 인덱스는 버린다.
    for i in range(P):
        start = require[i][0]
        end = require[i][1]
        cost = require[i][2]
        delta[start] += cost
        delta[end+1] -= cost

    










    for _ in range(P):
        start, end, cost = map(int,input().split())
        delta[start] += cost
        delta[end+1] -= cost

    current_delta= 0 #현재 시점의 변화량
    for i in range(N):
        current_delta += delta[i]
        arr[i] += current_delta

    print(f'#{tc}',arr)

