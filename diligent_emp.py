T = int(input())
for tc in range(1,T+1):
    H,W = map(int,input().split())
    matrix = []
    for _ in range(H):
        numbers = list(map(int,input().split()))
        matrix.append(numbers)

    count_zero = [0]*10000001
    for i in range(H):
        for j in range(W):
            count_zero[matrix[i][j]] += 1

    max_val = max(count_zero)
    max_index = count_zero.index(max_val)
    print(f'#{tc} {max_index}')

