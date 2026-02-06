# T = int(input())
#
# for tc in range(1,T+1):
#     N,K = map(int,input().split())
#     sample = list(map(int, input().split()))
#     code = list(map(int,input().split()))
#     #여기까지 숫자 입력받기 완료
#
#     j=0
#     check = 0
#     for x in sample:
#         if j<K and x == code[j]:
#             j += 1
#             if j == K:
#                 check += 1
#                 break
#
#     print(f'#{tc} {check}')
#
#         # elif j<K and  x != code[j]:
#         #     continue
#         #
#         # else:
#         #     print(f'#{tc} 0')
#         #     break

#------------------------------
#해석 버전
import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1,T+1):
    N,K = map(int,input().split())
    sample = list(map(int, input().split()))
    code = list(map(int,input().split()))
    #여기까지 숫자 입력받기 완료

    result = 0
    target_idx = 0

    for i in range(N):
        #target이 가리키고 있는 숫자와, sample이 가리키고 있는 숫자가 같다면,
        # -- target_idx += 1
        if target_idx < K and sample[i] == code[target_idx]:
            target_idx += 1  # 다음 target을 찾으러 간다

            # code를 끝까지 다 찾았으면 성공
            if target_idx == K:
                result = 1
                break

    print(f"#{tc} {result}")
