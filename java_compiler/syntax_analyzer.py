# syntax_analyzer.py
# 20193574 정설희

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
        # <로 시작 안하면 입력 오류이다 (<COMMA> 이런식으로 들어옴)
        if i[0] != "<":
            print("ERROR) invalid input")
            break
        else:
            # < 빼고 다음 내용부터
            # , 나오면 그 앞까지 자른다
            name = i[1:].split(",")[0]
            # <COMMA> 같은 경우엔 ,가 없어서 split(',')가 되지 않아 name이 COMMA>가 됨
            if name[-1] == ">":
                # > 없애주기
                name = name[:-1]
            # to_terminal 딕셔너리에서 올바른 terminal 형식으로 convert 해준다
            terminal = to_terminal[name]
            # terminal_list 리스트 마지막 요소로 추가한다
            terminal_list.append(terminal)

# state를 저장할 stack
# 시작 state는 0 번이다
stack_state = [0]

# terminal이나 non-terminal을 저장할 stack
stack_item = []

# terminal_list 마지막에 input의 끝을 알리는 $를 붙여준다
terminal_list.append("$")

# input 어디까지 읽었는지 알려줄 index
index = 0

while True:
    # input을 끝까지 읽었는데 acc가 나오지 않으면, while문 탈출해준다
    if index == len(terminal_list):
        print("REJECT) not accept")
        break
    try:
        # 현재 읽을 terminal을 terminal_list에서 꺼내와서, stack 최 상단 state와 match해 slr_table에서 다음 action을 꺼내온다
        action = slr_table[stack_state[-1]][terminal_list[index]]  
    except:
        print("REJECT) slr테이블상에 해당하는 action값이 없습니다 : on line", index)
        break
    if action == "acc":
        # acc가 들어왔는데, input이 남아있으면 reject
        if index != len(terminal_list):
            print("REJECT) input이 남아있습니다!")
        # 남은 input이 없으면 accept
        else:
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
        # 해당 cfg 문법을 꺼내서 cfg_list에 저장한다
        cfg_list = cfg[reduce_num]
        # RHS가 ''일 경우,  pop하지 않는다
        if cfg_list[-1] != "''":
            cfg_num = len(cfg_list) - 1
            # RHS 에 있는 item의 개수만큼 stack 에서 pop해준다
            for i in range(cfg_num):
                stack_state.pop()
                tmp_item = stack_item.pop()
                # stack에서 pop해낸 item과 CFG RHS의 item과 같지 않으면 reject해준다
                if tmp_item != cfg_list[-1-i]:
                    print("REJECT) on line",index)
        # LHS의 non_terminal을 stack_item의 마지막에 추가해준다
        stack_item.append(cfg_list[0])
        stack_state.append(slr_table[stack_state[-1]][cfg_list[0]])

fi.close()