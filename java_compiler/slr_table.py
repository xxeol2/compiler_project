slr_table = [
    # STATE 0
    {
        "vtype" : "s5",
        "class" : "s6",
        "$" : "r4",
        "CODE" : 1,
        "VDECL" : 2,
        "CDECL" : 4
    },
    # STATE 1
    {
        "$" : "acc"
    },
    # STATE 2 
    {
        "vtype": "s5",
        "class" : "s6",
        "$" : "r4",
        "CODE" : 7,
        "VDECL" : 2,
        "FDECL" : 3,
        "CDECL" : 4
    },
    # STATE 3
    {
        "vtype" : "s5",
        "class" : "s6",
        "$" : "r4",
        "CODE" : 8,
        "VDECL" : 2,
        "FDECL" : 3,
        "CDECL" : 4
    },
    # STATE 4 
    {
        "vtype" : "s5",
        "class" : "s6",
        "$" : "r4",
        "CODE" : 9,
        "VDECL" : 2,
        "FDECL" : 3,
        "CDECL" : 4
    },
    # STATE 5 
    {
        "id":"s10",
        "ASSIGN" : 11
    },
    # STATE 6 
    {
        "id":"s12"
    },
    # STATE 7 
    {
        "$" : "r1"
    },
    # STATE 8 
    {
        "$" : "r2"
    },
    # STATE 9 
    {
        "$" : "r3"
    },
    # STATE 10
    {
        "assign" : "s15",
        "semi" : "s13",
        "lparen" : "s14"
    },
    # STATE 11
    {
        "semi" : "s16"
    },
    # STATE 12
    {
        "lbrace" : "s17"
    },
    # STATE 13
    {
        "vtype": "r5",
        "id" : "r5",
        "rbrace": "r5",
        "if" : "r5",
        "while" : "r5",
        "return" : "r5",
        "class" : "r5",
        "$" : "r5"
    },
    # STATE 14
    {
        "vtype": "s19",
        "rparen" : "r21",
        "ARG" : 18
    },
    # STATE 15
    {
        "id" : "s28",
        "literal" : "s22",
        "character": "s23",
        "boolstr": "s24",
        "lparen" : "s27",
        "num": "s29",
        "RHS" : 20,
        "EXPR" : 21,
        "EXPR1" : 25,
        "EXPR2" : 26
    },
    # STATE 16
    {
        "vtype": "r6",
        "id" : "r6",
        "rbrace": "r6",
        "if" : "r6",
        "while" : "r6",
        "return" : "r6",
        "class" : "r6",
        "$" : "r6"
    },
    # STATE 17
    {
        "vtype": "s5",
        "rbrace": "r39",
        "VDECL" : 31,
        "FDECL" : 32,
        "ODECL" : 30
    },
    # STATE 18
    {
        "rparen" : "s33"
    },
    # STATE 19
    {
        "id" : "s34"
    },
    # STATE 20
    {
        "semi" : "r7"
    },
    # STATE 21
    {
        "semi" : "r8",
        "addsub" : "s35"
    },
    # STATE 22
    {
        "semi" : "r9"
    },
    # STATE 23
    {
        "semi" : "r10"
    },
    # STATE 24
    {
        "semi" : "r11"
    },
    # STATE 25
    {
        "semi" : "r13",
        "addsub" : "r13",
        "multdiv" : "s36",
        "rparen" : "r13"
    },
    # STATE 26
    {
        "semi" : "r15",
        "addsub" : "r15",
        "multdiv" : "r15",
        "rparen" : "r15"
    },
    # STATE 27
    {
        "id" : "s28",
        "lparen" : "s27",
        "num": "s29",
        "EXPR" : 37,
        "EXPR1" : 25,
        "EXPR2" : 26
    },
    # STATE 28
    {
        "semi" : "r17",
        "addsub" : "r17",
        "multdiv" : "r17",
        "rparen" : "r17"
    },
    # STATE 29
    {
        "semi" : "r18",
        "addsub" : "r18",
        "multdiv" : "r18",
        "rparen" : "r18"
    },
    # STATE 30
    {
        "rbrace": "s38"
    },
    # STATE 31
    {
        "vtype": "s5",
        "rbrace": "r39",
        "VDECL" : 31,
        "FDECL" : 32,
        "ODECL" : 39
    },
    # STATE 32
    {
        "vtype": "s5",
        "rbrace": "r39",
        "VDECL" : 31,
        "FDECL" : 32,
        "ODECL" : 40
    },
    # STATE 33
    {
        "lbrace" : "s41"
    },
    # STATE 34
    {
        "rparen" : "r23",
        "comma" : "s43",
        "MOREARGS" : 42
    },
    # STATE 35
    {
        "id" : "s28",
        "lparen" : "s27",
        "num": "s29",
        "EXPR1" : 44,
        "EXPR2" : 26
    },
    # STATE 36
    {
        "id" : "s28",
        "lparen" : "s27",
        "num": "s29",
        "EXPR2" : 45
    },
    # STATE 37
    {
        "addsub" : "s35",
        "rparen" : "s46"
    },
    # STATE 38
    {
        "vtype": "r36",
        "class" : "r36",
        "$" : "r36"
    },
    # STATE 39
    {
        "rbrace": "r37"
    },
    # STATE 40
    {
        "rbrace": "r38"
    },
    # STATE 41
    {
        "vtype": "s53",
        "id" : "s54",
        "rbrace": "r25",
        "if" : "s51",
        "while" : "s52",
        "return" : "r25",
        "VDECL" : 49,
        "ASSIGN" : 50,
        "BLOCK" : 47,
        "STMT" : 48
    },
    # STATE 42
    {
        "rparen" : "r20"
    },
    # STATE 43
    {
        "vtype": "s55"
    },
    # STATE 44
    {
        "semi" : "r12",
        "addsub" : "r12",
        "multdiv" : "s36",
        "rparen" : "r12"
    },
    # STATE 45
    {
        "semi" : "r14",
        "addsub" : "r14",
        "multdiv" : "r14",
        "rparen" : "r14"
    },
    # STATE 46
    {
        "semi" : "r16",
        "addsub" : "r16",
        "multdiv" : "r16",
        "rparen" : "r16"
    },
    # STATE 47
    {
        "return" : "s57",
        "RETURN" : 56
    },
    # STATE 48
    {
        "vtype": "s53",
        "id" : "s54",
        "rbrace": "r25",
        "if" : "s51",
        "while" : "s52",
        "return" : "r25",
        "VDECL" : 49,
        "ASSIGN" : 50,
        "BLOCK" : 58,
        "STMT" : 48
    },
    # STATE 49
    {
        "vtype": "r26",
        "id" : "r26",
        "rbrace": "r26",
        "if" : "r26",
        "while" : "r26",
        "return" : "r26"
    },
    # STATE 50
    {
        "semi" : "s59"
    },
    # STATE 51
    {
        "lparen" : "s60"
    },
    # STATE 52
    {
        "lparen" : "s61"
    },
    # STATE 53
    {
        "id" : "s62",
        "ASSIGN" : 11
    },
    # STATE 54
    {
        "assign" : "s15"
    },
    # STATE 55
    {
        "id" : "s63"
    },
    # STATE 56
    {
        "rbrace": "s64"
    },
    # STATE 57
    {
        "id" : "s28",
        "literal" : "s22",
        "character": "s23",
        "boolstr": "s24",
        "lparen" : "s27",
        "num": "s29",
        "RHS" : 65,
        "EXPR" : 21,
        "EXPR1" : 25,
        "EXPR2" : 26
    },
    # STATE 58
    {
        "rbrace": "r24",
        "return" : "r24"
    },
    # STATE 59
    {
        "vtype": "r27",
        "id" : "r27",
        "rbrace": "r27",
        "if" : "r27",
        "while" : "r27",
        "return" : "r27"
    },
    # STATE 60
    {
        "boolstr": "s67",
        "COND" : 66
    },
    # STATE 61
    {
        "boolstr": "s67",
        "COND" : 68
    },
    # STATE 62
    {
        "semi" : "s13",
        "assign" : "s15"
    },
    # STATE 63
    {
        "rparen" : "r23",
        "comma" : "s43",
        "MOREARGS" : 69
    },
    # STATE 64
    {
        "vtype": "r19",
        "rbrace": "r19",
        "class" : "r19",
        "$" : "r19"
    },
    # STATE 65
    {
        "semi" : "s70"
    },
    # STATE 66
    {
        "rparen" : "s71",
        "comp" : "s72"
    },
    # STATE 67
    {
        "rparen" : "r31",
        "comp" : "r31"
    },
    # STATE 68
    {
        "rparen" : "s73",
        "comp" : "s72"
    },
    # STATE 69
    {
        "rparen" : "r22"
    },
    # STATE 70
    {
        "rbrace": "r35"
    },
    # STATE 71
    {
        "lbrace" : "s74"
    },
    # STATE 72
    {
        "boolstr": "s76",
        "COND1" : 75
    },
    # STATE 73
    {
        "lbrace" : "s77"
    },
    # STATE 74
    {
        "vtype": "s53",
        "id" : "s54",
        "rbrace": "r25",
        "if" : "s51",
        "while" : "s52",
        "return" : "r25",
        "VDECL" : 49,
        "ASSIGN" : 50,
        "BLOCK" : 78,
        "STMT" : 48
    },
    # STATE 75
    {
        "rparen" : "r30",
        "comp" : "r30"
    },
    # STATE 76
    {
        "rparen" : "r32",
        "comp" : "r32"
    },
    # STATE 77
    {
        "vtype": "s53",
        "id" : "s54",
        "rbrace": "r25",
        "if" : "s51",
        "while" : "s52",
        "return" : "r25",
        "VDECL" : 49,
        "ASSIGN" : 50,
        "BLOCK" : 79,
        "STMT" : 48
    },
    # STATE 78
    {
        "rbrace": "s80"
    },
    # STATE 79
    {
        "rbrace": "s81"
    },
    # STATE 80
    {
        "vtype": "r34",
        "id" : "r34",
        "rbrace": "r34",
        "if" : "r34",
        "while" : "r34",
        "else" : "s83",
        "return" : "r34",
        "ELSE" : 82
    },
    # STATE 81
    {
        "vtype": "r29",
        "id" : "r29",
        "rbrace": "r29",
        "if" : "r29",
        "while" : "r29",
        "return" : "r29"
    },
    # STATE 82
    {
        "vtype": "r28",
        "id" : "r28",
        "rbrace": "r28",
        "if" : "r28",
        "while" : "r28",
        "return" : "r28"
    },
    # STATE 83
    {
        "lbrace" : "s84"
    },
    # STATE 84
    {
        "vtype": "s53",
        "id" : "s54",
        "rbrace": "r25",
        "if" : "s51",
        "while" : "s52",
        "return" : "r25",
        "VDECL" : 49,
        "ASSIGN" : 50,
        "BLOCK" : 85,
        "STMT" : 48
    },
    # STATE 85
    {
        "rbrace": "s86"
    },
    # STATE 86
    {
        "vtype": "r33",
        "id" : "r33",
        "rbrace": "r33",
        "if" : "r33",
        "while" : "r33",
        "return" : "r33"
    },
]