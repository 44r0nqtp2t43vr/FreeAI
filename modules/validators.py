def validate_L0_04(statement_type, tags_list):
    var_name_index = [tagged_word[1] for tagged_word in tags_list].index('var_name')
    if len(tags_list) == 3 and (statement_type == 'assignment' and tags_list[var_name_index][0] == 'repaircode'):
        return True
    return False