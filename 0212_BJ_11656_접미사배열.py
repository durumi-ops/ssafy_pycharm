S = input()

# 접미사 배열을 저장해둘 빈 리스트를 만들어둔다.
arr = []


# 문자열 S에 대하여 처음부터 +1씩 증가하는 범위로 문자를 제거하여 리스트에 넣어둔다.
for i in range(len(S)):
    arr.append(S[i:])

ans = sorted(arr)

for i in range(len(ans)):
    print(ans[i])