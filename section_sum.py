T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    # 여기까지 숫자 입력받기

    matrix = []
    for i in range(N - M + 1):
        num_sum = numbers[i]
        for j in range(1, M):
            num_sum += numbers[i + j]

        matrix.append(num_sum)

    max_val = max(matrix)
    min_val = min(matrix)

    print(f'#{tc} {max_val - min_val}')
