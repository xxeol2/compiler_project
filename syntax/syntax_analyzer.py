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

token_list = data.split('\n') # 한 줄 씩 나눠주기

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
            terminal = to_terminal[name]
            terminal_list.append(terminal)

stack = ["0"]

terminal_list.append("$")
print(terminal_list)

# print(slr_table[0][terminal_list[0]], terminal_list[0])
# print(slr_table[5][terminal_list[1]], terminal_list[1])
# print(slr_table[10][terminal_list[2]], terminal_list[2])
# print(slr_table[14][terminal_list[3]], terminal_list[3])
# print(slr_table[19][terminal_list[4]], terminal_list[4])
# print(slr_table[34][terminal_list[5]], terminal_list[5])

index = 0

while True:
    action = slr_table[stack[-1]][terminal_list[index]]
    if 
# terminal_list = ['vtype', 'id', 'lparen', 'vtype', 'id', 'rparen', 'lbrace', 'return', 'num', 'semi', 'rbrace', '$']

