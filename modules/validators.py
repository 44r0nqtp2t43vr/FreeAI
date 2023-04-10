def validate_L0_04(statement_type, tags_list):
    var_name_index = [tagged_word[1] for tagged_word in tags_list].index('var_name')
    if len(tags_list) == 3 and (statement_type == 'assignment' and (tags_list[var_name_index][0] == 'repaircode' and tags_list[0][1] == 'int')):
        return True
    return False

def validate_L0_05(statement_type, tags_list):
    tags = [tagged_word[1] for tagged_word in tags_list]
    var_name_index = tags.index('var_name')
    if len(tags_list) == 4 and (statement_type == 'assignment' and (var_name_index == 0 and 'number' in tags)):
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
    if len(tags_list) == 5 and (statement_type == 'assignment' and (tags_list[var_name_index][0] == 'freeai' and (tags_list[0][1] == 'int' and 'number' in tags))):
        return True
    return False