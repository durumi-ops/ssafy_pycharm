import sys
sys.stdin = open('input.txt','r')

N = int(input())

numbers=[list(map(int,input().split())) for _ in range(N)]

#N값 입력받아 배열 하기
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        print(numbers[i][j],end=' ')
    print()

print('------------------------------------')
# 시작점 (0,0에서 3*3 배열 합 구하기)
def cal(sy,sx):
    total = 0
    for i in range(sy,sy+3):
        for j in range(sx,sx+3):
            if i > 4 or i < 0 or j > 4 or j < 0:
                continue
            else:
                total += numbers[i][j]
    return(total)



max_val = 0
max_y = 0
max_x = 0

for y in range(N):
    for x in range(N):
        #total을 따로 설정하는 이유: 해당 좌표값을 저장하기 위해서.
        total = cal(y,x)
        if total > max_val:
            max_val = total
            max_y = y
            max_x = x


print(max_val)
print(f'({max_y}, {max_x})')


# 시작점에 대하여 반복문으로 순환시키기
# for x in range(N):
#     for y in range(N):
#         cal(x,y)