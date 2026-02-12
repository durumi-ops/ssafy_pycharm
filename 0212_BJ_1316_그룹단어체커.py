# import sys
# sys.stdin = open('input.txt','r')


# 그룹단어 여부 체크하는 함수를 만든다.
def check(word):
    status = 1
    for i in range(1,len(word)):
        if word[i] != word[i-1]:        # 만약 연속하는 두 문자가 다르다면
            if word[i] in word[:i-1]:   # 해당 문자가 그 전까지 문자 범위에서 한번이라도 등장했다면
                status = 0              # status = 0으로 변경

    return status

# N에 대하여 입력값을 받을건데,
N = int(input())

# N만큼 문자열을 입력받는다.
arr = [ input() for _ in range(N) ]

# 정답을 입력할 ans 리스트를 생성해둔다.
ans = []

# 입력받은 단어들에 대해 그룹단어 여부를 체크해본다.
for ch in arr:
    ans.append(check(ch))

# 그룹단어 개수를 센 후 출력한다.
print(ans.count(1))

