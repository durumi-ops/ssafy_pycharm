T = int(input())
for tc in range(1,T+1):
    H,W = map(int,input().split())
    normal_list = []
    for _ in range(H):
        normal_list.append(list(map(int,input().split())))

    bh, bw= map(int,input().split())
    black_list = []
    for _ in range(bh):
        black_list.append(list(map(int,input().split())))
    #모든 종류의 정보 입력받기 완료

    # 블랙리스트에 대한 인덱스만 1로 표시한 리스트 만들기
    is_blacklist = [0] * 100001
    for row in black_list:
        for num in row:
            is_blacklist[num] = 1


    count_blacklist = 0
    for row in normal_list:
        for num in row:
            if is_blacklist[num] == 1:
                count_blacklist += 1

    print(f'#{tc} {count_blacklist} {(H*W)-count_blacklist}')


