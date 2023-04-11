def validate_L0_04(statement_type, tags_list):
    var_name_index = [tagged_word[1] for tagged_word in tags_list].index('var_name')
    if len(tags_list) == 3 and (statement_type == 'assignment' and (tags_list[var_name_index][0] == 'repaircode' and tags_list[0][1] == 'int')):
        return True
    return False

def validate_L0_05(statement_type, tags_list):
    tags = [tagged_word[1] for tagged_word in tags_list]
    var_name_index = tags.index('var_name')
    if len(tags_list) == 4 or len(tags_list) == 5 and (statement_type == 'assignment' and (var_name_index == 0 and 'number' in tags)):
        return True
    return False

def validate_L0_06(statement_type, tags_list):
    tags = [tagged_word[1] for tagged_word in tags_list]
    var_name_index = tags.index('var_name')
    number_index = tags.index('number')
    if len(tags_list) == 5 and (statement_type == 'assignment' and (tags_list[var_name_index][0] == 'exitcode' and (tags_list[number_index][0] == '136' and tags_list[0][1] == 'int'))):
        return True
    return False

def validate_L0_19(statement_type, tags_list):
    tags = [tagged_word[1] for tagged_word in tags_list]
    var_name_index = tags.index('var_name')
    operator_index = tags.index('operator_ari')
    numbers_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == 'number']
    if len(tags_list) == 7 and (statement_type == 'assignment' and (tags_list[var_name_index][0] == 'thinking' and (len(numbers_indices) == 2 and (tags_list[numbers_indices[0]][0] == '2' and (tags_list[numbers_indices[0]][0] == tags_list[numbers_indices[1]][0] and (tags_list[operator_index][0] == '+' and tags_list[0][1] == 'int')))))):
        return True
    return False

def validate_L0_20(statement_type, tags_list):
    tags = [tagged_word[1] for tagged_word in tags_list]
    var_name_index = tags.index('var_name')
    operator_index = tags.index('operator_ari')
    number_index = tags.index('number')
    if len(tags_list) == 5 and (statement_type == 'assignment' and (tags_list[var_name_index][0] == 'thinking' and (tags_list[operator_index][0] == '/' and tags_list[number_index][0] == '2'))):
        return True
    return False

def validate_L0_21(statement_type, tags_list):
    tags = [tagged_word[1] for tagged_word in tags_list]
    var_name_index = tags.index('var_name')
    increment_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == '-']
    if len(tags_list) == 4 and (statement_type == 'assignment' and (tags_list[var_name_index][0] == 'thinking' and (len(increment_indices) == 2 and (tags_list[increment_indices[0]][0] == '-' and tags_list[increment_indices[0]][0] == tags_list[increment_indices[1]][0])))):
        return True
    return False

def validate_L0_27(statement_type, tags_list):
    tags = [tagged_word[1] for tagged_word in tags_list]
    var_name_index = tags.index('var_name')
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