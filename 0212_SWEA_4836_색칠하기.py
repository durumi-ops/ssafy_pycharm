import sys
sys.stdin = open('input.txt','r')



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]


    # 각 색깔별 빈 리스트를 먼저 생성해둔다.
    red_list=[]
    blue_list=[]

    for i in range(len(arr)):
        # 입력받은 리스트를 색으로 구분해둔다.

        if arr[i][4]==1:    # 만약 빨간색이라면,
            for k in range(arr[i][0],arr[i][2]+1): # r1~r2에 대하여
                for j in range(arr[i][1],arr[i][3]+1): # c1~c2에 대하여
                    red_list.append((k,j)) # red_list에 순서쌍으로 추가한다.


        else:               # 만약 파란색이라면,
            for k in range(arr[i][0],arr[i][2]+1): # r1~r2에 대하여
                for j in range(arr[i][1],arr[i][3]+1):  # c1~c2에 대하여
                    blue_list.append((k,j)) # red_list에 순서쌍으로 추가한다.

    # 더 작은 칸수를 가진 색이 무엇인지 파악하고
    min_len = min(len(blue_list),len(red_list))

    # 겹치는 색을 카운트할 초기값 cnt를 0으로 설정하고 시작한다.
    cnt = 0

    # 만약 blue가 더 많다면
    if len(blue_list)>len(red_list):
        for i in range(min_len):            # (더 적은) 빨간색에 대하여 red_list 안의 순서쌍이
            if red_list[i] in blue_list:    # blue_list 안에 들어있다면 (=겹치는게 있다면)
                cnt += 1                    # cnt +1 을 한다.
    else:
        for i in range(min_len):            # (더 적은) 파란색에 대하여 blue_list 안의 순서쌍이
            if blue_list[i] in red_list:    # red_list 안에 들어있다면 (=겹치는게 있다면)
                cnt += 1                    # cnt +1 을 한다.

    print(f'#{tc} {cnt}')                              # 최종 겹치는 색 cnt를 출력한다.




