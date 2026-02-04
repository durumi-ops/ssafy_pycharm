for tc in range(1,11):
    dump = int(input()) # 덤프 횟수 입력받기
    box_list = list(map(int,input().split())) # 박스 높이 입력받기

    for i in range(dump):
        min_val = min(box_list)
        max_val = max(box_list)
        box_list[box_list.index(min_val)] += 1
        box_list[box_list.index(max_val)] -= 1

        if (max_val - min_val) <= 1:
            break

    print(f'#{tc} {max(box_list)-min(box_list)}')

