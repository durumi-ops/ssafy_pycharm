# 재귀함수 구현
# - 시작지점
# - 종료지점
# - 누적된값


arr = [5, 2, 3, 4, 1]


# 1. 5 2 3 4 1 순서대로 출력하는 재귀함수를 구현하시오
# - 시작지점: 인덱스 0
# - 종료지점: 인덱스 4
# - 누적된값: 인덱스
def recur(idx):
    if idx == 4:
        print(arr[idx], end=' ')
        return

    print(arr[idx], end=' ')
    recur(idx + 1)  # 다음 인덱스를 전달하면서 다음 재귀호출

recur(0)
print()




# 2. 5 2 3 4 1 4 3 2 5 순서대로 출력하는 재귀함수를 구현하시오
# - 시작지점: 인덱스 0
# - 종료지점: 인덱스 4
# - 누적된값: 인덱스
def recur2(idx):
    if idx == 4:
        print(arr[idx], end=' ')
        return

    print(arr[idx], end=' ')  # 재귀 호출 전
    recur2(idx + 1)           # 다음 재귀 호출
    print(arr[idx], end=' ')  # 되돌아오면서 할 작업


recur2(0)