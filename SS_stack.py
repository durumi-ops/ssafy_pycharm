'''
괄호 검사 문젲 풀기
'''

def check_brackets(expression):
    stack = []  #빈 스택 리스트를 만들어둔다

    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack)==0 #모든 글자를 다 봤을 때 스택이 비어있어야 True

case1 = "(())()" # 정상적인 경우
case2 = "(()"   # 열린 괄호가 더 많은 경우
case3 = "())"   # 닫힌 괄호가 더 많은 경우

print(f"case1 결과: {check_brackets(case1)}") # True 출력
print(f"case2 결과: {check_brackets(case2)}") # False 출력
print(f"case3 결과: {check_brackets(case3)}") # False 출력