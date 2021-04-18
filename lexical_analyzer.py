# 20193574 정설희
# compiler - lexical analyzer(java)


####### 파일 명 입력받고 파일 열기 #######
s = input()
fi = open(s,'r') #input file
data = fi.read()

fo = open(s[:-5]+"_output.txt",'w') #output file

result = ""
lineNum= 1

####### nonZero(1..9) / Digits(0..9) / letters(a..zA..Z) / Escape 선언 #######
nonZero = list(range(ord('1'),ord('9')+1))
for i in range(0,len(nonZero)):
    nonZero[i] = chr(nonZero[i])

Digits = nonZero + ['0']

Letters = list(range(ord('a'),ord('z')+1)) + list(range(ord('A'),ord('Z')+1))
for i in range(0,len(Letters)):
    Letters[i] = chr(Letters[i])

Escape = "nrtb'\"\\"

# 공백으로 시작하는지 판단
def isSpace(data):
    global lineNum
    if data[0].isspace():
        if data[0] == '\n':
            lineNum +=1
        return True
    return False

def whiteSpace_scanner(data):
    if isSpace(data):
        try:
            return data[1:]
        except IndexError:
            return []
    return data

# <INTEGER> 토큰 판별 scanner
def integer_scanner(data):
    global result
    try:       
        if data[0]=='0': #(T0,0)->T1
            result += "<INTEGER, " + data[0] + ">\n"
            try:
                return data[1:]
            except IndexError: # 0으로 끝나면
                return []

        elif data[0]=='-': # (T0,-)->T2
            if data[1] in nonZero: # (T2,nonZero)->T3
                i = 2
                try:
                    while data[i] in Digits: # (T3,digit)->T4 / (T4.digit)->T4
                        i += 1
                except IndexError: # 끝까지 digit이면
                    result += "<INTEGER, " + data[0:i] + ">\n"
                    return []
                # digit이 아닌 다른게 오면
                result += "<INTEGER, " + data[0:i] + ">\n"
                return data[i:]        

        elif data[0] in nonZero: # (T0,nonZero)->T3
            i = 1
            try:
                while data[i] in Digits: # (T3,digit)->T4 / (T4,digit)->T4
                    i+=1
            except IndexError: # 끝까지 digit이면
                result += "<INTEGER, " + data[0:i] + ">\n"
                return []
            # digit이 아닌 다른게 오면
            result += "<INTEGER, " + data[0:i] + ">\n"
            return data[i:]
        
        return data
    except IndexError:
        return data

# <CHARACTER> 토큰 판별 scanner
def character_scanner(data):
    global result
    try:
        if data[0]=='\'': # (T0,')->T1
            try:
                if data[1]=='\\': # (T1,\)->T3
                    if data[2] in Escape: # (T3,escape)->T4
                        if data[3] == '\'': # (T4,')->T5
                            result += "<CHARACTER, " + data[1:3] + ">\n"
                            try:
                                return data[4:]
                            except IndexError:
                                return []
                    else:
                        result = "ERROR) character format error (line " + str(lineNum) +")"
                        return []
                elif data[1] in "'\"\\":
                    result = "ERROR) character format error (line " + str(lineNum) +")"
                    return []

                # (T1,single)->T2

                elif data[2]=='\'': # (T2,')->T5
                    result += "<CHARACTER, " + data[1] + ">\n"
                    try:
                        return data[3:]
                    except IndexError:
                        return []

                # (T2, not ') -> ERROR        
                else:
                    result = "ERROR) character format error (line " + str(lineNum) +")"
                    return []
            except IndexError:
                result = "ERROR) character format error (line " + str(lineNum) +")"
                return []
        return data
    except IndexError:
        return data

# <LITERAL> 토큰 판별 scanner
def literal_scanner(data):
    global result
    try:
        if data[0]=='"': # (T0,")->T1
            try:
                i = 1
                while True:
                    if data[i]!='"': # (T1,character)->T2 / (T2,character)->T2
                        i+=1
                    else: # (T1,")->T3 / (T2,")->T3
                        break
                result += "<LITERAL, " + data[0:i+1] + ">\n"
                try:
                    return data[i+1:]
                except IndexError:
                    return []
            except IndexError: # 끝날 때 까지 "가 나오지 않으면 literal format error
                result = "ERROR) literal format error (line " + str(lineNum) +")"
                return []
        return data
    except IndexError:
        return data

# <ID> 토큰 판별 scanner
def id_scanner(data):
    global result
    try:
        if data[0]=='_' or data[0] in Letters: # (T0,_)->T1
            i = 1
            try:
                while (data[i] in Digits) or (data[i] in Letters) or data[i]=='_': # (T1,_)->T1 / (T1,letter)->T1 / (T1,digit)->T1
                    i+=1
            except IndexError:
                result += "<ID, " + data[0:i] + ">\n"
                return []
            result += "<ID, " + data[0:i] + ">\n"
            return data[i:]
        return data
    except IndexError:
        return data

# 특정 키워드인지 판별하는 scanner (int -> <INT>, char -> <CHAR>, boolean -> <BOOLEAN>, ...)
def keyword_scanner(data): 
    global result
    try:
        if data[0:3] == 'int':
            try:
                if isSpace(data[3:]):
                    result += "<INT>\n"
                    return data[3:]
            except IndexError:
                result += "<INT>\n"
                return []
        elif data[0:4] == 'char':
            try:
                if isSpace(data[4:]):
                    result += "<CHAR>\n"
                    return data[4:]
            except IndexError:
                result += "<CHAR>\n"
                return []
        elif data[0:7]=='boolean':
            try:
                if isSpace(data[7:]):
                    result += "<BOOLEAN>\n"
                    return data[7:]
            except IndexError:
                result += "<BOOLEAN>\n"
                return []
        elif data[0:6]=='String':
            try:
                if isSpace(data[6:]):
                    result += "<STRING>\n"
                    return data[6:]
            except IndexError:
                result += "<STRING>\n"
                return []
        elif data[0:4]=='true':
            try:
                if isSpace(data[4:]):
                    result += "<TRUE>\n"
                    return data[4:]
            except IndexError:
                result += "<TRUE>\n"
                return []
        elif data[0:5]=='false':
            try:
                if isSpace(data[5:]):
                    result += "<FALSE>\n"
                    return data[5:] 
            except IndexError:    
                result += "<FALSE>\n"
                return []
        elif data[0:2]=='if':
            try:
                if isSpace(data[2:]):
                    result += "<IF>\n"
                    return data[2:]
            except IndexError:
                result += "<IF>\n"
                return []
        elif data[0:4]=='else':
            try:
                if isSpace(data[4:]):
                    result += "<ELSE>\n"
                    return data[4:]
            except IndexError:
                result += "<ELSE>\n"
                return []
        elif data[0:5]=='while':
            try:
                if isSpace(data[5:]):
                    result += "<WHILE>\n"
                    return data[5:]
            except IndexError:
                result += "<WHILE>\n"
                return []
        elif data[0:5]=='class':
            try:
                if isSpace(data[5:]):
                    result += "<CLASS>\n"
                    return data[5:]
            except IndexError:
                result += "<CLASS>\n"
                return []
        elif data[0:6]=='return':
            try:
                if isSpace(data[6:]):
                    result += "<RETURN>\n"
                    return data[6:]  
            except IndexError:
                result += "<RETURN>\n"
                return []
        return data
    except IndexError:
        return data


# <ARITH> <ASSIGN> <COMP> 토큰 판별 sscanner
def operator_scanner(data):
    global result
    try:
        if data[0]=='+':
            result += "<ARITH, " + data[0] + ">\n"
            try:
                return data[1:]
            except IndexError:
                return []
        elif data[0]=='-':
            result += "<ARITH, " + data[0] + ">\n" 
            try:
                return data[1:]
            except IndexError:
                return []
        elif data[0]=='*':
            result += "<ARITH, " + data[0] + ">\n" 
            try:
                return data[1:]
            except IndexError:
                return []
        elif data[0]=='/':
            result += "<ARITH, " + data[0] + ">\n" 
            try:
                return data[1:]
            except IndexError:
                return []
        elif data[0]=='=':
            try:
                if data[1]=='=':
                    result += "<COMP, " + data[0:2] + ">\n" 
                    try:
                        return data[2:]
                    except IndexError:
                        return []
                else:
                    result += "<ASSIGN>\n"
                    return data[1:]
            except IndexError:
                result += "<ASSIGN>\n"
                # print("<ASSIGN>")
                return []
        elif data[0]=='<':
            try:
                if data[1]=='=':
                    result += "<COMP, " + data[0:2] + ">\n"
                try:
                    return data[2:]
                except IndexError:
                    return []
                else:
                    result += "<COMP, " + data[0] + ">\n"
                    return data[1:]
            except IndexError:
                result += "<COMP, " + data[0] + ">\n"
                return []
        elif data[0]=='>':
            try:
                if data[1]=='=':
                    result += "<COMP, " + data[0:2] + ">\n"
                try:
                    return data[2:]
                except IndexError:
                    return []
                else:
                    result += "<COMP, " + data[0] + ">\n"
                    return data[1:]
            except IndexError:
                result += "<COMP, " + data[0] + ">\n"
                return []
        elif data[0]=='!':
            try:
                if data[1]=='=':
                    result += "<COMP, " + data[0:2] + ">\n"
                try:
                    return data[2:]
                except IndexError:
                    return []
            except IndexError:
                print("input Error : !")
                return []
        return data
    except IndexError:
        return data

def semi_scanner(data):
    global result
    try:
        if data[0]==';':
            result += "<SEMI>\n"
            # print("<SEMI>")
            try:
                return data[1:]
            except IndexError:
                return []
        return data
    except IndexError:
        return data

def bracket_scanner(data):
    global result
    try:
        if data[0]=='{':
            result += "<LSCOPE>\n"
            # print("<LSCOPE>")
            try:
                return data[1:]
            except IndexError:
                return []
        elif data[0]=='}':
            result += "<RSCOPE>\n"
            # print("<RSCOPE>")
            try:
                return data[1:]
            except IndexError:
                return []
        elif data[0]=='(':
            result += "<LPAREN>\n"
            # print("<LPAREN>")
            try:
                return data[1:]
            except IndexError:
                return []
        elif data[0]==')':
            result += "<RPAREN>\n"
            # print("<RPAREN>")
            try:
                return data[1:]
            except IndexError:
                return []
        elif data[0]=='[':
            result += "<LARR>\n"
            # print("<LARR>")
            try:
                return data[1:]
            except IndexError:
                return []
        elif data[0]==']':
            result += "<RARR>\n"
            # print("<RARR>")
            try:
                return data[1:]
            except IndexError:
                return []
        return data
    except IndexError:
        return data

def comma_scanner(data):
    global result
    try:
        if data[0]==',':
            result += "<COMMA>\n"
            # print("<COMMA>")
            try:
                return data[1:]
            except IndexError:
                return []
        return data
    except IndexError:
        return data

def scanner(data):
    # data = comma_scanner(arr_scanner(paren_scanner(scope_scanner(semi_scanner(operator_scanner(literal_scanner(character_scanner(integer_scanner(id_scanner(keyword_scanner(whiteSpace_scanner(data))))))))))))
    data = integer_scanner(data)
    return data

def test(data):
    data = comma_scanner(bracket_scanner(semi_scanner(operator_scanner(id_scanner(literal_scanner(character_scanner(integer_scanner(keyword_scanner(whiteSpace_scanner(data))))))))))
    # data = character_scanner(integer_scanner(whiteSpace_scanner(data)))
    try:
        test(data)
    except IndexError:
        return 0



# data = input()
# test(data)

test(data)
fo.write(result)
fi.close()
fo.close()

# f = open('test.java','r')

# def main():
#     data = input()
#     test(data)

# if __name__ == "__main__":
#     main()



#integer_scanner(data)
#character_scanner(data)
# integer_scanner(whiteSpace_scanner(integer_scanner(data)))
    