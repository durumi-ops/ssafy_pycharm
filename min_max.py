T = int(input())
for tc in range(1,T+1):
    num = int(input())
    matrix = list(map(int,input().split()))
    max_val = max(matrix)
    min_val = min(matrix)

    print(f'#{tc} {max_val-min_val}')
