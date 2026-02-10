import sys
sys.setrecursionlimit(10**6)

# 약수들의 합 구조
# N//2로 연산 횟수를 확 줄인다음, N//2에 대하여 num을 1부터 증가시키며 (N//2)%num == 0 이면 약수 리스트에 포함시키고 아니면 NO
# num 이 N//2보다 커지면 중단한다.
# while True:
# 명시적인 중단 명령(break)이 나올 때까지 내부 코드를 무한히 반복 실행
# 횟수를 모를 때 무한히 반복해야 하는 작업에 주로 사용됩니다.

arr_list = []

def recur(num,arr_list):
    if num > N//2:              # 종료 조건 : num이 N//2 보다 커지면 애초에 성립을 안하니까.
        return arr_list         # 약수 담긴 arr_list 반환하고 끝낸다.

    if N//2 % num == 0:         # num이 N//2의 약수라면
        arr_list.append(num)    # 약수를 약수리스트 arr_list에 담겠다.

    return recur(num+1,arr_list)# num+1을 하고 다시 실행해본다



# -1을 입력하기 전까지 N에 대하여 입력받는다.
while True:
    N = int(input())
    if N == -1:
        break

    sum_list = recur(1,[])      # 입력받은 N에 대하여 약수 리스트를 저장한 sum_list를 만든다.

    if sum(sum_list) != N:
        print(f'{N} is NOT perfect.')

    else:
        print(f'{N} = {" + ".join(map(str,sum_list))}')   # sum_list 안에 있는 숫자들을 str 으로 변환하여 '+'으로 결합하여 출력한다.
        #변수가 들어있는 함수 자체도 {}안에 넣어야 한다.
