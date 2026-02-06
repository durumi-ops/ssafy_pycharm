N = int(input())
arr = [ list(input()) for _ in range(N)]

for i in range(N):
    score = list([0]*len(arr[i])) #0으로 구성된 점수표 초기 세팅
    if arr[i][0] == 'O':
        score[0] = 1
    else:
        score[0] = 0


    for j in range(1,len(arr[i])):
        if arr[i][j] == 'O':
            if arr[i][j-1] == 'O':
                score[j] = score[j-1] + 1
            else:
                score[j] = 1
        else:
            continue

    print(sum(score))

