arr = [5, 1, 4, 2, 3]

# [문제 1]
# 정수 리스트를 오름차순으로 정렬하세요.
# - list.sort() 를 사용할 것
# - 원본 리스트가 변경되는지 확인하세요
# - 반환값이 있는지 확인하세요
# Todo: 이곳에 정렬 코드를 작성하세요

print("기본 리스트:", arr)
# 아래의 차이점은?

# arr.sort() : 원본 리스트를 직접 정렬 (원본을 건드려도 된다면 사용)
# result = sorted(arr) : 정렬된 새로운 리스트를 반환 (원본을 건드리지 말아야 된다면 사용)

# 내림차순일때는?
# result= sorted(arr, reverse = True)
# print(result)






words = ["apple", "banana", "kiwi"]

# [문제 2]
# 문자열 리스트를 "문자열 길이" 기준으로 오름차순 정렬하세요.
# - key 옵션을 반드시 사용하세요
# - lambda 식을 사용하세요
# - 각 원소의 길이를 어떻게 꺼낼지 고민해보세요
# Todo: 이곳에 정렬 코드를 작성하세요
# lambda: 일회용 함수를 쓰기 위해 사용하는 키워드
# lambda 파라미터: return 값
# 예시:
# add_func = lamda a, b: a+b
#print(add_func(20,30)) -> 50출력

#lambda를 통해 정렬 기준을 재정의한다.
# -x: 하나하나의 원소
# - len(x): 원소의 길이(정렬기준)
words.sort(key=lambda x: len(x))
print("문자열 리스트:", words)







data = [(1, 90), (3, 80), (2, 90)]
#data.sort() -> 데이터 순서대로 보면서 정렬 (앞에꺼부터 정렬한후 > 뒤에꺼 정렬)

# [문제 3-1]
# 튜플 리스트를 기본 정렬 기준으로 정렬하세요.
# - key 옵션 없이 정렬했을 때 어떤 값이 기준이 되는지 확인하세요
# Todo: 이곳에 정렬 코드를 작성하세요

result1 = sorted(data)
print(result1)

# [문제 3-2]
# 튜플의 두 번째 값(점수)을 기준으로 오름차순 정렬하세요.
# - lambda 를 사용하세요
# - x[1] 이 의미하는 바를 생각해보세요
# Todo: 이곳에 정렬 코드를 작성하세요
result2= sorted(data, key=lambda x:x[1])


# [문제 3-3]
# 점수 오름차순, 점수가 같으면 첫 번째 값 오름차순으로 정렬하세요.
# - key 에서 튜플을 반환하도록 작성하세요
# Todo: 이곳에 정렬 코드를 작성하세요
# 정렬기준이 2개 (1번을 기준으로 정렬한 후, 2번을 기준으로 재정렬)
result3= sorted(data, key=lambda x: (x[1],x[0]))
print(result3)




# [문제 3-4]
# 점수는 내림차순, 첫 번째 값은 오름차순으로 정렬하세요.
# - 숫자 내림차순을 어떻게 표현하는지 고민해보세요
# Todo: 이곳에 정렬 코드를 작성하세요

data = [(1,90),(3,80),(1,50),(2,90)]
result4= sorted(data, key=lambda x:(-x[1], x[0]))
#-를 붙이면 '내림차순'으로 정렬된다.
print("튜플 리스트:", data)


scores = {
    "kim": 90,
    "lee": 85,
    "park": 90
}

# [문제 4-1]
# 딕셔너리를 key 기준으로 정렬하세요.
# - dict 자체는 정렬되지 않음을 기억하세요
# - items() 를 사용해야 하는 이유를 생각해보세요
# Todo: 이곳에 정렬 코드를 작성하세요

# [문제 4-2]
# 딕셔너리를 value 기준으로 오름차순 정렬하세요.
# - lambda 에서 x[0], x[1] 이 각각 무엇인지 확인하세요
# Todo: 이곳에 정렬 코드를 작성하세요

# [문제 4-3]
# value 기준 내림차순으로 정렬하세요.
# - reverse 옵션을 사용할지, key 에서 처리할지 고민해보세요
# Todo: 이곳에 정렬 코드를 작성하세요

print("딕셔너리:", scores)


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"{self.name}:{self.score}"


students = [
    Student("kim", 90),
    Student("lee", 85),
    Student("park", 90)
]

# [문제 5-1]
# Student 객체 리스트를 점수 기준 오름차순으로 정렬하세요.
# - 객체 자체는 비교가 불가능함을 떠올리세요
# - key 에서 어떤 값을 반환해야 할지 생각해보세요
# Todo: 이곳에 정렬 코드를 작성하세요

# [문제 5-2]
# 점수는 내림차순, 이름은 오름차순으로 정렬하세요.
# - 다중 기준 정렬입니다
# - 튜플을 반환하는 key 를 작성하세요
# Todo: 이곳에 정렬 코드를 작성하세요

print("학생 객체 리스트:", students)