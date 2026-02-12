# ### 주사위 던져서 나온 결과 출력 (for문 쓰지 않고 출력하기) ###
#
# K = 3
#
# # 시작: 주사위 하나도 안던짐
# # 끝: 주사위 K개를 던짐
# # 누적값
# #   cnt: 던진 횟수
# #   path: 던진 주사위 기록
#
# def recur(cnt,path):
#     if cnt == K:
#         print(path)
#         return
#     for i in range(1,7):
#         path.append(i)
#         recur(cnt+1,path)
#         path.pop()
#
#
# recur(0, [])

###################################################################

### 전체 부분집합을 출력하는 재귀함수를 출력하자
#시작: 0개의 데이터를 부분집합에 넣을지 말지 고려
#끝: 모든 데이터를 부분집합에 넣을지 말지 고려
#누적값:
    # cnt: 몇개의 데이터를 고려했는가?
    # subset: 현재 부분집합


# arr = ['A', 'B', 'C', 'D']
#
#
# def recur2(idx, subset):
#     if idx == len(arr):
#         print(subset)
#         return
#
#     #1. 현재 원소를 부분집합에 포함
#     subset.append(arr[idx])
#     recur2(idx+1,subset)
#     subset.pop()
#
#     #2. 현재 원소를 부분집합에 포함 X
#     recur2(idx+1,subset)
#
# recur2(0,[])

######################################################################

### 순열 : 전체 중 K개를 순서를 고려하면서 골라서 문제를 해결

# - 순열
#  - 전체 중 K개를 순서를 고려하면서 골라서 문제를 해결


arr = ['A', 'B', 'C', 'D']
K = 3

# - 중복 순열 (같은 걸 여러 번 골라도 된다)
# 예시) AAA ~ DDD 까지 구해보기

# 시작: 0개의 알파벳을 선택
# 끝: K개의 알파벳을 선택
# 누적값
#   - cnt: 현재까지 고른 알파벳의 개수
#   - path: 현재까지 고른 알파벳
def recur3(cnt, path):
    if cnt == K:
        print(*path)
        return

    for i in range(len(arr)):
        path.append(arr[i])
        recur3(cnt + 1, path)
        path.pop()

recur3(0, [])

# - 순열
#   - 중복 순열 코드에서 중복을 없애는 코드만 추가

used = [0] * len(arr)

def recur4(cnt, path):
    if cnt == K:
        print(*path)
        return

    for i in range(len(arr)):
        if used[i]:  # 이미 i를 사용한 적이 있다면 continue
            continue

        used[i] = 1
        path.append(arr[i])
        recur4(cnt + 1, path)
        path.pop()
        used[i] = 0  # 쓴 적이 없다고 초기화

recur4(0, [])