# text = 'ddz=z='
# sample = 'z='
# text = text.strip(sample)
# print(text)

# 초기 문자열 입력받는다.
word = input()

#크로아티아 알파벳 목록을 만들어둔다.
format_list = ['c=','c-','dz=','d-','lj','nj','s=','z=']

# 세야하는 문자 개수를 초기값 = 0 설정 후
count = 0

# 크로아티아 문자를 카운팅 해서 초기값에 더하고 + 해당 문자들은 모두 지운다.
for i in range(len(format_list)):
    count += word.count(format_list[i])
    word = word.replace(format_list[i],' ') # word.strip(format_list[i])로 했더니 해당 자리를 유지하지 않고 지워버려서 계산 오류 발생
    #(예: 'dz='를 삭제하는 상황에서 'd   z='이 아니라 'dz='으로 word를 출력해버림.


# 남은 (일반) 알파벳에 대하여 문자 개수 구한 후 초기값에 누적하여 더한다.

print(len(word))
# count += len(word) 하면 안돼 -> 왜냐면 크로아티아 알파벳을 공백으로 처리해둔 상태이기 때문에, 그것도 같이 카운팅을 하게 됨.

# format_list = ['c=','c-','dz=','d-','lj','nj','s=','z=']
# for i in range(len(format_list)):
