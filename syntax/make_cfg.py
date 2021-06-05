data = """START -> CODE
CODE -> VDECL CODE
CODE -> FDECL CODE
CODE -> CDECL CODE
CODE -> ''
VDECL -> vtype id semi
VDECL -> vtype ASSIGN semi
ASSIGN -> id assign RHS
RHS -> EXPR
RHS -> literal
RHS -> character
RHS -> boolstr
EXPR -> EXPR addsub EXPR1
EXPR -> EXPR1
EXPR1 -> EXPR1 multdiv EXPR2
EXPR1 -> EXPR2
EXPR2 -> lparen EXPR rparen
EXPR2 -> id
EXPR2 -> num
FDECL -> vtype id lparen ARG rparen lbrace BLOCK RETURN rbrace
ARG -> vtype id MOREARGS
ARG -> ''
MOREARGS -> comma vtype id MOREARGS
MOREARGS -> ''
BLOCK -> STMT BLOCK
BLOCK -> ''
STMT -> VDECL
STMT -> ASSIGN semi
STMT -> if lparen COND rparen lbrace BLOCK rbrace ELSE
STMT -> while lparen COND rparen lbrace BLOCK rbrace
COND -> COND comp COND1
COND -> boolstr
COND1 -> boolstr
ELSE -> else lbrace BLOCK rbrace
ELSE -> ''
RETURN -> return RHS semi
CDECL -> class id lbrace ODECL rbrace
ODECL -> VDECL ODECL
ODECL -> FDECL ODECL
ODECL -> ''"""

line = data.split('\n')
result = []
for i in line:
    tmplst = i.split(' ')
    tmplst.remove('->')
    result.append(tmplst)

print(result)