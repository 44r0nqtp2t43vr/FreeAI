def validate_L0_04(statement_type, tags_list):
    var_name_index = [tagged_word[1] for tagged_word in tags_list].index('var_name')
    if len(tags_list) == 3 and (statement_type == 'assignment' and (tags_list[var_name_index][0] == 'repaircode' and tags_list[0][1] == 'int')):
        return True
    return False

def validate_L0_05(statement_type, tags_list):
    tags = [tagged_word[1] for tagged_word in tags_list]
    if 'var_name' in tags:
        var_name_index = tags.index('var_name')
    else:
        return False
    if len(tags_list) == 4 or len(tags_list) == 5 and (statement_type == 'assignment' and (var_name_index == 0 and 'number' in tags)):
        return True
    return False

def validate_L0_06(statement_type, tags_list):
    tags = [tagged_word[1] for tagged_word in tags_list]
    if 'var_name' in tags and 'number' in tags:
        var_name_index = tags.index('var_name')
        number_index = tags.index('number')
    else:
        return False
    if len(tags_list) == 5 and (statement_type == 'assignment' and (tags_list[var_name_index][0] == 'exitcode' and (tags_list[number_index][0] == '136' and tags_list[0][1] == 'int'))):
        return True
    return False

def validate_L0_19(statement_type, tags_list):
    tags = [tagged_word[1] for tagged_word in tags_list]
    if 'var_name' in tags and 'operator_ari' in tags:
        var_name_index = tags.index('var_name')
        operator_index = tags.index('operator_ari')
    else:
        return False
    numbers_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == 'number']
    if len(tags_list) == 7 and (statement_type == 'assignment' and (tags_list[var_name_index][0] == 'thinking' and (len(numbers_indices) == 2 and (tags_list[numbers_indices[0]][0] == '2' and (tags_list[numbers_indices[0]][0] == tags_list[numbers_indices[1]][0] and (tags_list[operator_index][0] == '+' and tags_list[0][1] == 'int')))))):
        return True
    return False

def validate_L0_20(statement_type, tags_list):
    tags = [tagged_word[1] for tagged_word in tags_list]
    if 'var_name' in tags and 'operator_ari' in tags and 'number' in tags:
        var_name_index = tags.index('var_name')
        operator_index = tags.index('operator_ari')
        number_index = tags.index('number')
    else:
        return False
    if len(tags_list) == 5 and (statement_type == 'assignment' and (tags_list[var_name_index][0] == 'thinking' and (tags_list[operator_index][0] == '/' and tags_list[number_index][0] == '2'))):
        return True
    return False

def validate_L0_21(statement_type, tags_list):
    tags = [tagged_word[1] for tagged_word in tags_list]
    if 'var_name' in tags:
        var_name_index = tags.index('var_name')
    else:
        return False
    increment_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == '-']
    if len(tags_list) == 4 and (statement_type == 'assignment' and (tags_list[var_name_index][0] == 'thinking' and (len(increment_indices) == 2 and (tags_list[increment_indices[0]][0] == '-' and tags_list[increment_indices[0]][0] == tags_list[increment_indices[1]][0])))):
        return True
    return False

def validate_L0_27(statement_type, tags_list):
    tags = [tagged_word[1] for tagged_word in tags_list]
    if 'var_name' in tags:
        var_name_index = tags.index('var_name')
    else:
        return False
    if len(tags_list) == 5 or len(tags_list) == 6 and (statement_type == 'assignment' and (tags_list[var_name_index][0] == 'freeai' and (tags_list[0][1] == 'int' and 'number' in tags))):
        return True
    return False

def validate_L1_04(statement_type, tags_list):
    if statement_type != 'loop':
        return False
    tags = [tagged_word[1] for tagged_word in tags_list]
    if '!' in tags:
        conditioner = '!'
    elif 'operator_glt' in tags:
        conditioner = tags_list[tags.index('operator_glt')][0]
    else:
        return False
    if '+' in tags:
        increment = '+'
    elif '-' in tags:
        increment = '-'
    else:
        return False
    varname_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == 'var_name']
    number_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == 'number']
    function_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == 'function_name']
    if tags_list[0][0] == 'for' and (len(varname_indices) == 3 and (len(number_indices) == 2 and (len(function_indices) == 1))):
        if tags_list[function_indices[0]][0] != 'goright' or tags_list[number_indices[0]][0] != '0' or tags_list[number_indices[1]][0] != '4' or conditioner != '<' or increment != '+':
            return False
        if tags_list[varname_indices[0]][0] == 'i' and (tags_list[varname_indices[0]][0] == tags_list[varname_indices[1]][0] and tags_list[varname_indices[0]][0] == tags_list[varname_indices[2]][0]):
            if int(tags_list[number_indices[0]][0]) < int(tags_list[number_indices[1]][0]) and (conditioner == '>' or increment == '-'):
                return False
            if int(tags_list[number_indices[0]][0]) > int(tags_list[number_indices[1]][0]) and (conditioner == '<' or increment == '+'):
                return False
            return True
    return False

def validate_L1_05(statement_type, tags_list):
    if statement_type != 'loop':
        return False
    tags = [tagged_word[1] for tagged_word in tags_list]
    if '!' in tags:
        conditioner = '!'
    elif 'operator_glt' in tags:
        conditioner = tags_list[tags.index('operator_glt')][0]
    else:
        return False
    if '+' in tags:
        increment = '+'
    elif '-' in tags:
        increment = '-'
    else:
        return False
    varname_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == 'var_name']
    number_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == 'number']
    function_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == 'function_name']
    if tags_list[0][0] == 'for' and (len(varname_indices) == 3 and (len(number_indices) == 2 and (len(function_indices) == 1))):
        if tags_list[varname_indices[0]][0] == 'i' and (tags_list[varname_indices[0]][0] == tags_list[varname_indices[1]][0] and tags_list[varname_indices[0]][0] == tags_list[varname_indices[2]][0]):
            if int(tags_list[number_indices[0]][0]) < int(tags_list[number_indices[1]][0]) and (conditioner == '>' or increment == '-'):
                return False
            if int(tags_list[number_indices[0]][0]) > int(tags_list[number_indices[1]][0]) and (conditioner == '<' or increment == '+'):
                return False
            return True
    return False

def validate_L1_13(statement_type, tags_list):
    equals_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == '=']
    varname_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == 'var_name']
    number_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == 'number']
    function_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == 'function_name']
    if statement_type == 'loop' and (len(equals_indices) == 2 and (len(varname_indices) == 1 and (len(number_indices) == 1 and len(function_indices) == 1))):
        if tags_list[varname_indices[0]][0] != 'hasnoright' or tags_list[function_indices[0]][0] != 'goright':
            return False
        if tags_list[0][1] == 'while' and (equals_indices[1] - equals_indices[0] == 1 and tags_list[number_indices[0]][0] == '0'):
            return True
    return False

def validate_L1_14(statement_type, tags_list):
    equals_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == '=']
    varname_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == 'var_name']
    number_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == 'number']
    function_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == 'function_name']
    if statement_type == 'loop' and (len(equals_indices) == 2 and (len(varname_indices) == 1 and (len(number_indices) == 1 and len(function_indices) == 1))):
        if tags_list[0][1] == 'while' and (equals_indices[1] - equals_indices[0] == 1 and tags_list[number_indices[0]][0] == '0'):
            if tags_list[varname_indices[0]][0] == 'hasnoright' and tags_list[function_indices[0]][0] == 'goright':
                return True
            elif tags_list[varname_indices[0]][0] == 'hasnoleft' and tags_list[function_indices[0]][0] == 'goleft':
                return True
            elif tags_list[varname_indices[0]][0] == 'hasnoup' and tags_list[function_indices[0]][0] == 'goup':
                return True
            elif tags_list[varname_indices[0]][0] == 'hasnodown' and tags_list[function_indices[0]][0] == 'godown':
                return True
    return False

def validate_L1_20(statement_type, tags_list):
    equals_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == '=']
    varname_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == 'var_name']
    number_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == 'number']
    function_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == 'function_name']
    if statement_type == 'loop' and (len(equals_indices) == 2 and (len(varname_indices) == 1 and (len(number_indices) == 1 and len(function_indices) == 1))):
        if tags_list[0][1] == 'do' and (equals_indices[1] - equals_indices[0] == 1 and tags_list[number_indices[0]][0] == '0'):
            if tags_list[varname_indices[0]][0] == 'hasnoright' and tags_list[function_indices[0]][0] == 'goright':
                return True
            elif tags_list[varname_indices[0]][0] == 'hasnoleft' and tags_list[function_indices[0]][0] == 'goleft':
                return True
            elif tags_list[varname_indices[0]][0] == 'hasnoup' and tags_list[function_indices[0]][0] == 'goup':
                return True
            elif tags_list[varname_indices[0]][0] == 'hasnodown' and tags_list[function_indices[0]][0] == 'godown':
                return True
    return False

def validate_L2_06(statement_type, tags_list):
    varname_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == 'var_name']
    equals_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == '=']
    number_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == 'number']
    function_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == 'function_name']
    if statement_type == 'conditional' and (len(equals_indices) == 2 and (len(varname_indices) == 1 and (len(number_indices) == 1 and len(function_indices) == 1))):
        if tags_list[0][1] == 'if' and (equals_indices[1] - equals_indices[0] == 1 and tags_list[number_indices[0]][0] == '1'):
            if tags_list[varname_indices[0]][0] == 'turn' and tags_list[function_indices[0]][0] == 'usewateroid':
                return True
    return False

def validate_L2_13(statement_type, tags_list):
    tags = [tagged_word[1] for tagged_word in tags_list]
    varname_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == 'var_name']
    equals_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == '=']
    number_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == 'number']
    function_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == 'function_name']
    if statement_type == 'conditional' and (len(equals_indices) == 2 and (len(varname_indices) == 1 and (len(number_indices) == 1 and len(function_indices) == 2))):
        if tags_list[0][1] == 'if' and ('else' in tags and (equals_indices[1] - equals_indices[0] == 1 and tags_list[number_indices[0]][0] == '1')):
            if tags_list[varname_indices[0]][0] == 'turn' and (tags_list[function_indices[0]][0] == 'useelectroid' and tags_list[function_indices[1]][0] == 'usefiroid'):
                return True
    return False

def validate_L2_21(statement_type, tags_list):
    varname_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == 'var_name']
    equals_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == '=']
    number_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == 'number']
    function_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == 'function_name']
    if_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == 'if']
    else_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == 'else']
    if statement_type == 'conditional' and (len(equals_indices) == 4 and (len(varname_indices) == 2 and (len(number_indices) == 2 and (len(function_indices) == 3 and (len(if_indices) == 2 and len(else_indices) == 2))))):
        if (equals_indices[1] - equals_indices[0] != 1) or (equals_indices[3] - equals_indices[2] != 1):
            return False
        if tags_list[number_indices[0]][0] != '70' or tags_list[number_indices[1]][0] != '421':
            return False
        if tags_list[varname_indices[0]][0] != 'turn' or tags_list[varname_indices[1]][0] != 'turn':
            return False
        if tags_list[function_indices[0]][0] != 'usefiroid' or tags_list[function_indices[1]][0] != 'usewateroid' or tags_list[function_indices[2]][0] != 'useelectroid':
            return False
        if if_indices[1] - else_indices[0] != 1:
            return False
        return True
    return False

def validate_L3_01(statement_type, tags_list):
    tags = [tagged_word[1] for tagged_word in tags_list]
    varname_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == 'var_name']
    function_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == 'function_name']
    if statement_type == 'function' and (len(varname_indices) == 1 and (len(function_indices) == 1 and ('int' in tags and 'number' in tags))):
        if tags_list[0][1] == 'void' and (tags_list[function_indices[0]][0] == 'repair' and tags_list[varname_indices[0]][0] == 'repaircode'):
            return True
    return False

def validate_L3_08(statement_type, tags_list):
    tags = [tagged_word[1] for tagged_word in tags_list]
    if 'operator_ari' in tags and 'number' in tags:
        operator_ari = tags_list[tags.index('operator_ari')][0]
        number = tags_list[tags.index('number')][0]
    else:
        return False
    int_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == 'int']
    varname_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == 'var_name']
    function_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == 'function_name']
    if statement_type == 'function' and (len(varname_indices) == 4 and (len(function_indices) == 1 and len(int_indices) == 3)):
        if tags_list[0][1] == 'int' and (tags_list[function_indices[0]][0] == 'getkey' and (operator_ari == '+' and number == '2')):
            if tags_list[varname_indices[0]][0] == 'humankey' and tags_list[varname_indices[2]][0] == 'humankey':
                if tags_list[varname_indices[1]][0] == 'finalkey' and tags_list[varname_indices[3]][0] == 'finalkey':
                    return True
    return False

def validate_L3_12(statement_type, tags_list):
    tags = [tagged_word[1] for tagged_word in tags_list]
    if 'operator_ari' in tags and 'number' in tags:
        operator_ari = tags_list[tags.index('operator_ari')][0]
        number = tags_list[tags.index('number')][0]
    else:
        return False
    int_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == 'int']
    varname_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == 'var_name']
    function_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == 'function_name']
    if statement_type == 'function' and (len(varname_indices) == 4 and (len(function_indices) == 1 and len(int_indices) == 3)):
        if tags_list[0][1] == 'int' and (tags_list[function_indices[0]][0] == 'getkey' and (operator_ari == '*' and number == '2')):
            if tags_list[varname_indices[0]][0] == 'humankey' and tags_list[varname_indices[2]][0] == 'humankey':
                if tags_list[varname_indices[1]][0] == 'finalkey' and tags_list[varname_indices[3]][0] == 'finalkey':
                    return True
    return False