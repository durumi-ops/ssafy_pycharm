'''
주유시, 기름이 어느정도 채워졌는지 알려주는 장치를 만들려고 합니다.
고객들이 많아 O(N) 으로 성능을 측정하면, 손님을 놓칠 수 있기 때문에 보다 빠른 성능으로 동작하는 프로그램을 작성해야합니다.

기름이 채워진 상태는 # 으로 채워지지 않은 상태는 _ 로 나타납니다
예를 들어, #####_____ (# 5개, _ 5개) 라면 50%가 채워진 상태입니다.

기름의 상태를 문자열로 입력 받아주세요.

 총 몇 % 연료가 채워졌는지 출력해 주세요.
'''
N = int(input().strip())

for tc in range(1,N+1):
    status = input().strip()

    # 전체 칸수와 '#' 개수를 찾기 위한 준비
    total_len = len(status)
    low = 0 # 가장 작은 인덱스
    high = total_len - 1 # 가장 큰 인덱스
    fuel_count = 0  # '#'이 몇 개인지 저장할 변수

    # 이진 탐색 (절반씩 뚝딱 나누기)
    while low <= high:
        mid = (low + high) // 2

        if status[mid] == '#':
            fuel_count = mid + 1  # 일단 여기까지는 기름이 찼음
            low = mid + 1  # 뒤쪽에 더 있나 확인
        else:
            high = mid - 1  # 앞쪽에 끝이 있나 확인

    # 3. 결과 계산 및 출력 (공식대로!)
    answer = (fuel_count * 100) // total_len
    print(f"#{tc} {answer}%")