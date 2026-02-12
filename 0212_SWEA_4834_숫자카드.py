v

T = int(input())

for tc in range(1,T+1):
    cnt = [0] * 10
    max_value = 0
    idx = 0
    N = int(input())   # N은 카드의 숫자
    num = input()       # num은 공백없이 입력받는 숫자
    for n in num:
        cnt[int(n)] += 1


    for i in range(10):
        if cnt[i] >= max_value:
            max_value = cnt[i]
            idx = i

    print(f'#{tc} {idx} {max_value}')


########### 틀린 버전 #############
"""
T = int(input())
cnt = [0]*10            #여기서 cnt = [0]*10 리스트를 만드니까 매번 테스트케이스 시행할 때마다 갱신이 안됨....

for tc in range(1,T+1):
    N = int(input())   # N은 카드의 숫자
    num = input()       # num은 공백없이 입력받는 숫자
    for n in num:
        cnt[int(n)] += 1
    cnt_max = max(cnt)
    idx_max = cnt.index(cnt_max)
    print(f'#{tc} {idx_max} {cnt_max}')
"""