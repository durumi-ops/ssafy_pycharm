voca = input() # 문자열 입력받는다.
new_voca = ''.join(voca.split())
new_voca_1 = ''.join(set(new_voca)) # 문자열 내/외 공백 제거

upper_voca = voca.upper()
dict_keys = new_voca_1.upper()

dict= {}
for chr in dict_keys:
    count = upper_voca.count(chr)
    dict[chr] = upper_voca.count(chr)


max_key = max(dict, key = dict.get)
max_list = [k for k,v in dict.items() if max(dict.values())==v]

if len(max_list)>1:
    print('?')
else:
    print(max_key)
#dict= {}
# for chr in new_voca:
#     count = voca.count('chr')
#     print(f'{chr}:{count}')