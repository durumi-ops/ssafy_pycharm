# arr = [list(input()) for _ in range(5)] : 이렇게 하면 오류 발생 (연속된 글자를 '한덩어리'로 생각하기 때문에)

# 글자 입력받기 (숫자, 문자 구분해두는)
arr = []
for _ in range(5):
    s = input()
    list = [] # **각 입력줄에 대하여 독립된 리스트를 만들려면 list=[]를 반복문 '안'에 넣어야 한다 (밖에 꺼내두면 오류 생김)
    for chr in s:
        if chr.isdigit():
            list.append(int(chr))
        else:
            list.append(chr)
    arr.append(list)
# print(arr)




max=0
for i in range(5):
    if len(arr[i])>max:
        max=len(arr[i])
#여기까지는 열의 최댓값 구하는 식
# print(max)



# 각 열에 대하여 행(아래) 방향으로 읽겠다.
for c in range(max):
    for r in range(5):
        if c >= len(arr[r]): #그 행의 열 개수보다 c가 커진다면 -> 오류 생길거니까(공백이니까) continue
            continue
        print(arr[r][c],end='')


