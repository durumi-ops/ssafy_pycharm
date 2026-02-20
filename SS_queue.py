from collections import deque

# 프린트 대기열에 대해 출력하는 함수를 정의한다.
def printer_simulation(doc_list):
    queue = deque(doc_list)     # 문서리스트를 큐로 변환
    print(f'현재 대기열: {list(queue)}')
    # queue를 list에 담지 않으면 deque(['보고서.pdf', '사진.jpg'])처럼 출력이 되기 때문에 가독성을 위해 list를 붙여준다.
    print('--------')

    while queue:    # queue에 대기열이 있을 때까지 실행
        current_doc = queue.popleft()
        print(f'인쇄중: {current_doc}')
        print(f'남은 대기열: {list(queue)}')

    # queue에 아무런 대기열도 없으면
    return '모든 문서 인쇄 완료'

docs = ["보고서.pdf", "사진.jpg", "메모.txt"]

result = printer_simulation(docs)
print(result)