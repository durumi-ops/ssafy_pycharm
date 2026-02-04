T = int(input())
for tc in range(1,T+1):
    num_card = int(input())
    card_list = list(map(int,input())) #붙어있는 값을 입력받으니까 .split() 하지 않아도 됨
    #여기까지 숫자 입력받기 완료

    zero_list = [0]*((max(card_list))+1)
    #card_list에서의 최댓값 +1 개 만큼으로 구성된 [0] 리스트 생성
    for num in card_list:
        zero_list[num] += 1
        #(주어진 입력값) card_list에서의 숫자를 인덱스로 받은 위치에 +1을 한다.

    max_num = zero_list.index(max(zero_list))
    #zero_list 에서의 최댓값 인덱스를 max_num 으로 받는다.
    max_num_count = max(zero_list)
    #zero_list에서의 최댓값을 max_num_count 으로 받는다.
    print(f'#{tc} {max_num} {max_num_count}')