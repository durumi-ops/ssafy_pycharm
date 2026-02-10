N = int(input())
arr=[]
# def cal(num):
#     if num <=1:
#         arr.append(1)
#         return 1
#
#     arr.append(num%2)
#     cal(num//2)
#     return arr
#
# print(*cal(N)[::-1])


N = int(input())
def recur(num):
    if num == 0:
        return


    recur(num//2) #2로 나눈 몫을 저장     #이게 가장 큰 재귀호출 그림(로직)
    print(num2, end='')

recur(N)