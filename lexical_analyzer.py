# 20193574 정설희
# compiler - lexical analyzer(java)


####### 파일 명 입력받고 파일 열기 #######
s = input()
fi = open(s,'r') #input file
data = fi.read()

fo = open(s[:-5]+"_output.txt",'w') #output file

result = "" #ouput txt에 쓰여질 문자열
lineNum= 1 #ERROR 몇번째 line에서 발생했는지 알기 위한 variable

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

# 공백 잘라주는 scanner
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

# <ARITH> <ASSIGN> <COMP> 토큰 판별 scanner
def operator_scanner(data):
    global result
    try:
        if data[0]=='+': # <ARITH> (T0,+)->T1
            result += "<ARITH, " + data[0] + ">\n"
            try:
                return data[1:]
            except IndexError:
                return []
        elif data[0]=='-': # <ARITH> (T0,-)->T2
            result += "<ARITH, " + data[0] + ">\n" 
            try:
                return data[1:]
            except IndexError:
                return []
        elif data[0]=='*': # <ARITH> (T0,*)->T3
            result += "<ARITH, " + data[0] + ">\n" 
            try:
                return data[1:]
            except IndexError:
                return []
        elif data[0]=='/': # <ARITH> (T0,/)->T4
            result += "<ARITH, " + data[0] + ">\n" 
            try:
                return data[1:]
            except IndexError:
                return []
        elif data[0]=='=': # <COMP> (T0,=)->T3 / <ASSIGN> (T0,=)->T1
            try:
                if data[1]=='=': # <COMP> (T3,=)->T4
                    result += "<COMP, " + data[0:2] + ">\n" 
                    try:
                        return data[2:]
                    except IndexError:
                        return []
                else: # <ASSIGN> T1
                    result += "<ASSIGN>\n"
                    return data[1:]
            except IndexError: # <ASSIGN> T1
                result += "<ASSIGN>\n"
                return []
        elif data[0]=='<': # <COMP> (T0,<)->T1
            try:
                if data[1]=='=': # <COMP> (T1,=)->T7
                    result += "<COMP, " + data[0:2] + ">\n"
                    try:
                        return data[2:]
                    except IndexError:
                        return []
                else: # <COMP> T1
                    result += "<COMP, " + data[0] + ">\n"
                    return data[1:]
            except IndexError: # <COMP> T1
                result += "<COMP, " + data[0] + ">\n"
                return []
        elif data[0]=='>': # <COMP> (T0,>)->T2
            try:
                if data[1]=='=': # <COMP> (T2,=)->T7
                    result += "<COMP, " + data[0:2] + ">\n"
                    try:
                        return data[2:]
                    except IndexError:
                        return []
                else: # <COMP> T2
                    result += "<COMP, " + data[0] + ">\n"
                    return data[1:]
            except IndexError: # <COMP> T2
                result += "<COMP, " + data[0] + ">\n"
                return []
        elif data[0]=='!': # <COMP> (T0,!)->T5
            try:
                if data[1]=='=': # <COMP> (T5,=)->T6
                    result += "<COMP, " + data[0:2] + ">\n"
                    try:
                        return data[2:]
                    except IndexError:
                        return []
                else: # <COMP> T5 format error
                    result = "ERROR) comparison operator format error (line " + str(lineNum) +")"
                    return []
            except IndexError:
                result = "ERROR) comparison operator format error (line " + str(lineNum) +")"
                return []
        return data
    except IndexError:
        return data

# <SEMI> 토큰 판별 scanner
def semi_scanner(data):
    global result
    try:
        if data[0]==';':
            result += "<SEMI>\n"
            try:
                return data[1:]
            except IndexError:
                return []
        return data
    except IndexError:
        return data

# 괄호 토큰 판별 scanner (<LPAREN> <RPAREN> <LSCOPE> <RSCOPE> <LARR> <RARR>)
def bracket_scanner(data):
    global result
    try:
        if data[0]=='{':
            result += "<LSCOPE>\n"
            try:
                return data[1:]
            except IndexError:
                return []
        elif data[0]=='}':
            result += "<RSCOPE>\n"
            try:
                return data[1:]
            except IndexError:
                return []
        elif data[0]=='(':
            result += "<LPAREN>\n"
            try:
                return data[1:]
            except IndexError:
                return []
        elif data[0]==')':
            result += "<RPAREN>\n"
            try:
                return data[1:]
            except IndexError:
                return []
        elif data[0]=='[':
            result += "<LARR>\n"
            try:
                return data[1:]
            except IndexError:
                return []
        elif data[0]==']':
            result += "<RARR>\n"
            try:
                return data[1:]
            except IndexError:
                return []
        return data
    except IndexError:
        return data

# <COMMA> 토큰 판별 scanner
def comma_scanner(data):
    global result
    try:
        if data[0]==',':
            result += "<COMMA>\n"
            try:
                return data[1:]
            except IndexError:
                return []
        return data
    except IndexError:
        return data


def test(data):
    global result
    data = comma_scanner(bracket_scanner(semi_scanner(operator_scanner(id_scanner(literal_scanner(character_scanner(integer_scanner(keyword_scanner(whiteSpace_scanner(data))))))))))
    try:
        test(data)
    except IndexError:
        return 0
    except:
        result =  "ERROR) input error (line " + str(lineNum) +")"


test(data)
fo.write(result)
fi.close()
fo.close()
