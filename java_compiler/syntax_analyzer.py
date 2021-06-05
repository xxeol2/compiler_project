from to_terminal import to_terminal
from slr_table import slr_table
from cfg import cfg

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

stack_state = [0]
stack_item = []

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
    
    if index == len(terminal_list):
        break
    try:
        action = slr_table[stack_state[-1]][terminal_list[index]]  
    except:
        print("ERROR) invalid input : ", index)
        break
    print("action", action)
    if action == "acc":
        print ("ACCEPT !!")
        break


    # shift 연산일 경우
    if action[0]=='s':
        # stack에 terminal 넣어주기
        stack_item.append(terminal_list[index])
        index += 1
        # stack에 state 넣어주기
        stack_state.append(int(action[1:]))

    # reduce 연산일 경우
    elif action[0] == 'r':
        reduce_num = int(action[1:])
        cfg_list = cfg[reduce_num]
        print("cfg", cfg_list)
        if cfg_list[-1] != "''":
            cfg_num = len(cfg_list) - 1
            for i in range(cfg_num):
                stack_state.pop()
                tmp_item = stack_item.pop()
                if tmp_item != cfg_list[-1-i]:
                    print("ERROR")
        stack_item.append(cfg_list[0])
        print(stack_item)
        stack_state.append(slr_table[stack_state[-1]][cfg_list[0]])
        print(stack_state)





# terminal_list = ['vtype', 'id', 'lparen', 'vtype', 'id', 'rparen', 'lbrace', 'return', 'num', 'semi', 'rbrace', '$']

