from to_terminal import to_terminal
from slr_table import slr_table

s = input()
try:
    fi = open(s,'r') #input file
except FileNotFoundError:
    print('파일이 없습니다.')
    quit()

# data에 저장
data = fi.read()
# print(data)
# print("#################")
token_list = data.split('\n') # 한 줄 씩 나눠주기
# print(token_list)
# print("#################")
terminal_list = []

# 토큰 하나씩 읽어오기
for i in token_list:
    if len(i) > 0:
        if i[0] != "<":
            print("ERROR")
            break
        else:
            name = i[1:].split(",")[0]
            if name[-1] == ">":
                name = name[:-1]
            print(name)
            terminal = to_terminal[name]
            terminal_list.append(terminal)

terminal_list.append("$")

print(terminal_list)
