import sys
sys.stdin = open('input.txt','r')

#1. 입력
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

print('-------------------------')

#2. 가로부터 접근
for y in range(5):
    for x in range(5):
        #print(y,x) # 좌표값 출력
        print(arr[y][x], end = ' ')
    print() #5개씩 끊어서 출력하려고 할 때

print('--------------------------')

#3. 세로부터 접근
for x in range(5):
    for y in range(5):
        print(arr[y][x], end=' ')
    print()

print('--------------------------')

#4. 대각선부터 접근

#4.1 우하단 대각선 (\)
for i in range(5):
    print(arr[i][i])

print('--------------------------')

#4.2 좌하단 대각선 (/)
for i in range(5):
    print(arr[i][4-i])

print('--------------------------')

#5. 범위 접근
#   3*3 사각형 범위
#   예시) 합이 가장 큰 3*3 범위 값을 구하여라.

total = 0
sx, sy = 0, 0
for y in range(sy, sy+3):
    for x in range(sx, sx+3):
        # 범위 밖 계산 체크를 항상 하도록 하자!!!

        # 1. 범위 밖은 계산하지 마라.
        if y > 4 or y < 0 or x > 4 or x < 0: #범위를 벗어났을 때
            continue # 아무 액션 하지 말고 다음으로 넘어가라.

        total += arr[y][x]

        #2. 범위 안에 들어왔을 때만 계산해라.
        #if 0 <= y <= 4 and 0<= x <=4:
        #    total += arr[y][x]
print(total)

print('--------------------------')
#5. 범위 접근 (최종_ver.)
#   3*3 사각형 범위
#   예시) 합이 가장 큰 3*3 범위 값을 구하여라.


#계산하고자 하는 출발지에 대하여 반복
#위에서 구하는 로직을 함수로 정의

def cal_total(sy, sx):
    total = 0
    for y in range(sy, sy + 3):  # 출발지 ~ 출발지 + 3
        for x in range(sx, sx + 3):
            # 범위 밖 계산 체크를 항상 합시다!
            # 1. [권장] 범위 밖은 계산하지 마라
            if y > 4 or y < 0 or x > 4 or x < 0:
                continue

            total += arr[y][x]

            # 2. 범위 안에 들어왔을 때만 계산해라
            #   - 추후 조건이 많아지면 가독성이 떨어진다.
            # if 0 <= y <= 4 and 0 <= x <= 4:
            #     total += arr[y][x]

    return total


max_total = 0
max_y, max_x = 0, 0

# 계산하고자 하는 출발지를 반복
for sy in range(5):
    for sx in range(5):
        total = cal_total(sy, sx)
        # max_total = max(max_total, total)  # 값만 필요하다면
        # 좌표값까지 같이 저장
        if total > max_total:
            max_total = total
            max_y = sy
            max_x = sx

print(max_y, max_x, max_total)


