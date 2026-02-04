for tc in range(1,11):
    N = int(input())
    building = list(map(int,input().split()))

    count = 0

    for i in range(2,N-2):
        neighbor = max(building[i-2], building[i-1], building[i+1],building[i+2])
        if building[i] > neighbor:
            count += building[i] - neighbor

    print(f'#{tc} {count}')



