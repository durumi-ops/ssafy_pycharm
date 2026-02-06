T = int(input())

for tc in range(1,T+1): #tc 케이스에 대하여
    N, M = map(int, input().split())
    arr = [list ((input())) for _ in range(N)] #N줄 만큼의 숫자를 입력받는다.

    answer='' #answer에 대해서 빈 값을 만들어둔다 (저장해두기 위해서)

    # 가로부터 체크
    for i in range(N):
        for j in range(0,N-M+1):
            part = arr[i][j:j+M]
            if part == part[::-1]:
                answer = ''.join(part)
                break
        if answer: #answer에 값이 있으면,
            break #바깥 for i 를 멈추기 위한 요소 (답이 있으면 바로 멈추게 하기 위해서)

    # 가로에 answer가 없을 때 -> 세로에서 찾고자 할 때
    if answer == '':
        for i in range(N):
            for j in range(0, N - M + 1):
                l=[arr[j+k][i] for k in range(M)]
                if l == l[::-1]:
                    answer = ''.join(l)
                    break
            if answer: #answer에 값이 있으면
                break

    print(f'#{tc} {answer}')

