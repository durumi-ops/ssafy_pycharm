T = int(input())
for tc in range(1,T+1):
    H,W = map(int,input().split())
    normal_list = []
    for _ in range(H):
        normal_list.append(list(map(int,input().split())))

    bh, bw = map(int,input().split())
    black_list = []
    for _ in range(bh):
        black_list.append(list(map(int,input().split())))

    #여기까지 일반주민, 블랙리스트 값 입력받기 완료

    count_zero = [0]*100001
