# 20193574 정설희
# compiler - lexical analyzer(java)


####### 파일 명 입력받고 파일 열기 #######
s = input()
fi = open(s,'r') #input file
fo = open(s[:-5]+"_output.txt",'w') #output file


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
    if data[0].isspace():
        return True
    return False

def whiteSpace_scanner(data):
    if isSpace(data):
        try:
            return data[1:]
        except IndexError:
            return []
    return data

def integer_scanner(data):
    try:       
        if data[0]=='0':
            try:
                print("<INTEGER, ",data[0],">",sep="")
                try:
                    return data[1:]
                except IndexError:
                    return []
            except IndexError:
                print("<INTEGER, ",data[0],">",sep="")
                return []
        elif data[0] in nonZero:
            i = 1
            try:
                while data[i] in Digits:
                    i+=1
            except IndexError:
                print("<INTEGER, ",data[0:i],">",sep="")
                return []
            print("<INTEGER, ",data[0:i],">",sep="")
            return data[i:]
        
        elif data[0]=='-':
            if data[1] in nonZero:
                i = 2
                try:
                    while data[i] in Digits:
                        i += 1
                except IndexError:
                    print("<INTEGER, ",data[0:i],">",sep="")
                    return []
                print("<INTEGER, ",data[0:i],">",sep="")
                return data[i:]
        return data
    except IndexError:
        return data

def character_scanner(data):
    try:
        if data[0]=='\'':
            try:
                if data[1]=='\\':
                    if data[2] in Escape:
                        if data[3] == '\'':
                            print("<CHARACTER, ", data[1:3],">",sep="")
                            try:
                                return data[4:]
                            except IndexError:
                                return []
                    else:
                        print("input Error : no character")
                        return []
                elif data[2]=='\'':
                    print("<CHARACTER, ",data[1], ">", sep="")
                    try:
                        return data[3:]
                    except IndexError:
                        return []
                else:
                    print("input Error : character")
                    return []
            except IndexError:
                print("input Error : no '")
                return []
        return data
    except IndexError:
        return data

def literal_scanner(data):
    try:
        if data[0]=='"':
            try:
                i = 1
                while True:
                    if data[i]!='"':
                        i+=1
                    else:
                        break
                print("<LITERAL, ",data[0:i+1],">",sep="")
                try:
                    return data[i+1:]
                except IndexError:
                    return []
            except IndexError:
                print("input Error : literal")
                return []
        return data
    except IndexError:
        return data

def id_scanner(data):
    try:
        if data[0]=='_' or data[0] in Letters:
            i = 1
            try:
                while (data[i] in Digits) or (data[i] in Letters) or data[i]=='_':
                    i+=1
            except IndexError:
                print("<ID, ",data[0:i],">",sep="")
                return []
            print("<ID, ",data[0:i],">",sep="")
            return data[i:]
        return data
    except IndexError:
        return data

# 특정 키워드인지 check (int, char, boolean, ...)
def keyword_scanner(data): 
    try:
        if data[0:3] == 'int':
            try:
                if isSpace(data[3:]):
                    print("<INT>")
                    return data[3:]
            except IndexError:
                print("<INT>")
                return []
        elif data[0:4] == 'char':
            try:
                if isSpace(data[4:]):
                    print("<CHAR>")
                    return data[4:]
            except IndexError:
                print("<CHAR>")
                return []
        elif data[0:7]=='boolean':
            try:
                if isSpace(data[7:]):
                    print("<BOOLEAN>")
                    return data[7:]
            except IndexError:
                print("<BOOLEAN>")
                return []
        elif data[0:6]=='String':
            try:
                if isSpace(data[6:]):
                    print("<STRING>")
                    return data[6:]
            except IndexError:
                print("<STRING>")
                return []
        elif data[0:4]=='true':
            try:
                if isSpace(data[4:]):
                    print("<TRUE>")
                    return data[4:]
            except IndexError:
                print("<TRUE>")
                return []
        elif data[0:5]=='false':
            try:
                if isSpace(data[5:]):
                    print("<FALSE>")
                    return data[5:] 
            except IndexError:    
                print("<FALSE>")
                return []
        elif data[0:2]=='if':
            try:
                if isSpace(data[2:]):
                    print("<IF>")
                    return data[2:]
            except IndexError:
                print("<IF>")
                return []
        elif data[0:4]=='else':
            try:
                if isSpace(data[4:]):
                    print("<ELSE>")
                    return data[4:]
            except IndexError:
                print("<ELSE>")
                return []
        elif data[0:5]=='while':
            try:
                if isSpace(data[5:]):
                    print("<WHILE>")
                    return data[5:]
            except IndexError:
                print("<WHILE>")
                return []
        elif data[0:5]=='class':
            try:
                if isSpace(data[5:]):
                    print("<CLASS>")
                    return data[5:]
            except IndexError:
                print("<CLASS>")
                return []
        elif data[0:6]=='return':
            try:
                if isSpace(data[6:]):
                    print("<RETURN>")
                    return data[6:]  
            except IndexError:
                print("<RETURN>")
                return []
        return data
    except IndexError:
        return data

def operator_scanner(data):
    try:
        if data[0]=='+':
            print("<ARITH, ",data[0],">",sep="")
            try:
                return data[1:]
            except IndexError:
                return []
        elif data[0]=='-':
            print("<ARITH, ",data[0],">",sep="")
            try:
                return data[1:]
            except IndexError:
                return []
        elif data[0]=='*':
            print("<ARITH, ",data[0],">",sep="")
            try:
                return data[1:]
            except IndexError:
                return []
        elif data[0]=='/':
            print("<ARITH, ",data[0],">",sep="")
            try:
                return data[1:]
            except IndexError:
                return []
        elif data[0]=='=':
            try:
                if data[1]=='=':
                    print("<COMP, ",data[0:2],">",sep="")
                    try:
                        return data[2:]
                    except IndexError:
                        return []
                else:
                    print("<ASSIGN>")
                    return data[1:]
            except IndexError:
                print("<ASSIGN>")
                return []
        elif data[0]=='<':
            try:
                if data[1]=='=':
                    print("<COMP, ",data[0:2],">",sep="")
                try:
                    return data[2:]
                except IndexError:
                    return []
                else:
                    print("<COMP, ",data[0],">",sep="")
                    return data[1:]
            except IndexError:
                print("<COMP, ",data[0],">",sep="")
                return []
        elif data[0]=='>':
            try:
                if data[1]=='=':
                    print("<COMP, ",data[0:2],">",sep="")
                try:
                    return data[2:]
                except IndexError:
                    return []
                else:
                    print("<COMP, ",data[0],">",sep="")
                    return data[1:]
            except IndexError:
                print("<COMP, ",data[0],">",sep="")
                return []
        elif data[0]=='!':
            try:
                if data[1]=='=':
                    print("<COMP, ",data[0:2],">",sep="")
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
    try:
        if data[0]==';':
            print("<SEMI>")
            try:
                return data[1:]
            except IndexError:
                return []
        return data
    except IndexError:
        return data


def bracket_scanner(data):
    try:
        if data[0]=='{':
            print("<LSCOPE>")
            try:
                return data[1:]
            except IndexError:
                return []
        elif data[0]=='}':
            print("<RSCOPE>")
            try:
                return data[1:]
            except IndexError:
                return []
        elif data[0]=='(':
            print("<LPAREN>")
            try:
                return data[1:]
            except IndexError:
                return []
        elif data[0]==')':
            print("<RPAREN>")
            try:
                return data[1:]
            except IndexError:
                return []
        elif data[0]=='[':
            print("<LARR>")
            try:
                return data[1:]
            except IndexError:
                return []
        elif data[0]==']':
            print("<RARR>")
            try:
                return data[1:]
            except IndexError:
                return []
        return data
    except IndexError:
        return data


def comma_scanner(data):
    try:
        if data[0]==',':
            print("<COMMA>")
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


data = fi.read()
fo.write(data)
test(data)
fo.write("??")

# f = open('test.java','r')

# def main():
#     data = input()
#     test(data)

# if __name__ == "__main__":
#     main()



#integer_scanner(data)
#character_scanner(data)
# integer_scanner(whiteSpace_scanner(integer_scanner(data)))
    