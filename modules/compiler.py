import modules.validators as validator

lexicon_dict = {
    'int': ['int'],
    'var_name': ['repaircode', 'exitcode', 'thinking', 'freeai', 'i', 'hasnoright', 'hasnoleft', 'hasnoup', 'hasnodown'],
    'function_name': ['proceed', 'goright', 'goleft', 'goup', 'godown'],
    'number': [str(num) for num in range(1000)],
    'operator_ari': ['+', '-', '*', '/', '%'],
    'operator_glt': ['>', '<'],
    'operator_log': ['&&', '||'],
    'if': ['if'],
    'else': ['else'],
    'while': ['while'],
    'do': ['do'],
    'for': ['for'],
    'switch': ['switch'],
    'case': ['case'],
    'break': ['break'],
    'default': ['default'],
    '=': ['='],
    ':': [':'],
    ';': [';'],
    '(': ['('],
    ')': [')'],
    '{': ['{'],
    '}': ['}'],
    '!': ['!'],
    '+': ['+'],
    '-': ['-'],
}

grammar_dict = {
    'S': [['statement_list']],
    'statement_list': [['statement'], ['statement', 'statement_list']],
    'statement': [['assignment'], ['conditional'], ['loop'], ['function_call']],
    'assignment': [['int_ass'], ['increment', ';']],
    'conditional': [['cond_if'], ['cond_switch']],
    'loop': [['loop_while'], ['loop_do_while'], ['loop_for']],
    'int_ass': [['int', 'var_name', ';'], ['int', 'var_name', '=', 'value_list', ';'], ['var_name', 'operator_ass', 'value_list', ';']],
    'operator_ass': [['='], ['operator_ari', '=']],
    'operator_rel': [['=', '='], ['operator_glt'], ['!', '='], ['operator_glt', '=']],
    'operator_inc': [['+', '+'], ['-', '-']],
    'number_all': [['-', 'number'], ['number']],
    'value_list': [['number_list'], ['var_list']],
    'number_list': [['number_all'], ['number_all', 'operator_ari', 'value_list']],
    'var_list': [['var_name'], ['var_name', 'operator_ari', 'value_list']],
    'else_list': [['else', 'statement_block'], ['else', 'if', 'condition_block', 'statement_block', 'else_list']],
    'case_list': [['case_block'], ['default_block'], ['case_block', 'case_list']],
    'cond_if': [['if', 'condition_block', 'statement_block'], ['if', 'condition_block', 'assignment'], 
                ['if', 'condition_block', 'statement_block', 'else_list']],
    'cond_switch': [['switch', '(', 'var_name', ')', '{', 'case_list', '}']],
    'loop_while': [['while', 'condition_block', 'statement_block'], ['while', 'condition_block', 'assignment']],
    'loop_do_while': [['do', 'statement_block', 'while', 'condition_block', ';']],
    'loop_for': [['for', '(', 'int_ass', 'condition_list', ';', 'increment', ')', 'assignment'],
                 ['for', '(', 'int_ass', 'condition_list', ';', 'increment', ')', 'statement_block']],
    'increment': [['operator_inc', 'var_name'], ['var_name', 'operator_inc']],
    'condition': [['(', 'condition', ')'], ['!', '(', 'condition', ')'], ['value_list'], ['value_list', 'operator_rel', 'value_list']],
    'condition_list': [['condition'], ['condition', 'operator_log', 'condition_list'], ['(', 'condition', 'operator_log', 'condition_list', ')'], 
                      ['!', '(', 'condition', 'operator_log', 'condition_list', ')']],
    'case_block': [['case', 'number_all', ':', 'statement_list'], ['case', 'number_all', ':', 'statement_list', 'break', ';']],
    'default_block': [['default', ':', 'statement_list'], ['default', ':', 'statement_list', 'break', ';']],
    'condition_block': [['(', 'condition_list', ')']],
    'statement_block': [['{', 'statement_list', '}'], ['{', '}']],
    'function_call': [['function_name', '(', ')', ';']],
}

row_id = 0

class EarleyRow:
    def __init__(self, pid, chart, operator, start, end, symbol, production, cid = None):
        global row_id
        self.id = row_id
        row_id = row_id + 1
        self.pid = pid
        self.chart = chart
        self.operator = operator
        self.start = start
        self.end = end
        self.symbol = symbol
        self.production = production
        self.cid = cid
    
    def print_row(self):
        print(self.chart, self.id, self.pid, self.operator, self.start, self.end, self.symbol, self.production, self.cid)

class EarleyParser:
    def __init__(self, lexicon, grammar):
        self.lexicon = lexicon
        self.grammar = grammar
        self.terminals = [key for key in lexicon]
        self.nonterminals = [key for key in grammar]
        self.parsed = []

    def shift_dot(self, prod):
        if '*' in prod:
            index = prod.index('*')
            prod.remove('*')
            prod.insert(index + 1, '*')
            return prod

    def predict(self, earley_row):
        prod = getattr(earley_row, 'production')
        for child_prod in self.grammar[prod[prod.index('*') + 1]]:
            pid = getattr(earley_row, 'id') # parent id
            chart = getattr(earley_row, 'chart')
            end = getattr(earley_row, 'end')
            symbol = prod[prod.index('*') + 1]
            child_row = EarleyRow(pid, chart, 'PRED', end, end, symbol, ['*'] + child_prod)
            self.table.append(child_row)
            cr_prod = getattr(child_row, 'production')
            if cr_prod[cr_prod.index('*') + 1] in self.terminals:
                continue
            self.predict(child_row)
    
    def scan(self, earley_row, word):
        prod = getattr(earley_row, 'production')
        if word in self.lexicon[prod[prod.index('*') + 1]]:
            pid = getattr(earley_row, 'id')
            chart = getattr(earley_row, 'chart') + 1
            start = getattr(earley_row, 'start')
            end = getattr(earley_row, 'end') + 1
            symbol = prod[prod.index('*') + 1]
            self.table.append(EarleyRow(pid, chart, 'SCAN', start, end, symbol, [word, '*']))
            return True
        return False
    
    def complete(self, to_comp_row, comp_row):
        comp_symbol = getattr(comp_row, 'symbol')
        comp_prod = getattr(comp_row, 'production')
        while comp_symbol != 'S' and comp_prod[-1] == '*':
            last_cid = getattr(to_comp_row, 'cid')
            if last_cid != None:
                cid = [getattr(comp_row, 'id')] + last_cid
            else:
                cid = [getattr(comp_row, 'id')] + [last_cid]
            pid = getattr(to_comp_row, 'pid')
            chart = getattr(comp_row, 'chart')
            start = getattr(to_comp_row, 'start')
            end = getattr(comp_row, 'end')
            symbol = getattr(to_comp_row, 'symbol')
            prod = getattr(to_comp_row, 'production').copy()
            comp_row = EarleyRow(pid, chart, 'COMP', start, end, symbol, self.shift_dot(prod), cid)
            self.table.append(comp_row)
            comp_symbol = getattr(comp_row, 'symbol')
            comp_prod = getattr(comp_row, 'production')
            to_comp_row = ([row for row in self.table if row.id == pid])[0]
            
    
    def parse(self, sentence):
        sentence = sentence.split()
        self.tokens = sentence
        self.table = [EarleyRow(0, 0, 'PRED', 0, 0, 'y', ['*', 'S'])]
        self.predict(self.table[0])
        for index, word in enumerate(sentence):
            to_scan = [er for er in self.table if getattr(er, 'chart') == index and (getattr(er, 'production')[-1] != '*' and getattr(er, 'production')[getattr(er, 'production').index('*') + 1] in self.terminals)]
            for row in to_scan:
                has_scanned = self.scan(row, word)
                if has_scanned:
                    self.complete(row, self.table[-1])
                    comp_prod = getattr(self.table[-1], 'production')
                    comp_symbol = getattr(self.table[-1], 'symbol')
                    if  index == len(sentence) - 1 and (comp_symbol == 'S' and comp_prod[-1] == '*'):
                        break
                    if comp_prod[-1] != '*' and comp_prod[comp_prod.index('*') + 1] not in self.terminals:
                        self.predict(self.table[-1])
        # for row in self.table:
        #     row.print_row()
        if getattr(self.table[-1], 'symbol') == 'S' and getattr(self.table[-1], 'production')[-1] == '*':
            self.get_parsed()
            self.get_parsed_symbols()
            self.get_statement_type()
            self.get_tags_list()
            return True
        return False
    
    def get_parsed(self, to_get = None):
        if self.table == None:
            return
        if to_get == None:
            to_get = self.table[-1]
        to_get_cid = getattr(to_get, 'cid')
        if to_get_cid == None:
            self.parsed.append(to_get)
            # to_get.print_row()
            return
        for cid in to_get_cid:
            if cid == None:
                self.parsed.append(to_get)
                # to_get.print_row()
                return
            next_row = ([row for row in self.table if getattr(row, 'id') == cid])[0]
            self.get_parsed(next_row)
    
    def get_parsed_symbols(self):
        self.parsed_symbols = [getattr(row, 'symbol') for row in self.parsed]
        self.parsed_symbols.reverse()
        return self.parsed_symbols
    
    def get_statement_type(self):
        statement_types = [item for sublist in self.grammar['statement'] for item in sublist]
        for symbol in self.get_parsed_symbols():
            if symbol in statement_types:
                self.statement_type = symbol
                return
    
    def get_tags_list(self):
        tags_list = []
        parsed_symbols_terminals = [symbol for symbol in self.parsed_symbols if symbol in self.terminals]
        for index, token in enumerate(self.tokens):
            tags_list.append((token, parsed_symbols_terminals[index]))
        self.tags_list = tags_list
    
# parser = EarleyParser(lexicon_dict, grammar_dict)
# print(parser.parse('int my_int = 0 ;'))

lvl0_to_validate = [4, 5, 6, 19, 20, 21, 27]
lvl1_to_validate = [4, 5, 13, 14, 20]

def compile(code, screen_name, script_index):
    if code.strip() == '':
        return {'is_valid': False}
    preprocess_list = [['\n', ' '], ['\t', ' '], ['=', ' = '], [';', ' ; '], ['(', ' ( '], [')', ' ) '], ['{', ' { '], ['}', ' } '], ['+', ' + '], 
                       ['-', ' - '], ['*', ' * '], ['/', ' / '], ['%', ' % '], ['>', ' > '], ['<', ' < '], ['!', ' ! '] , [':', ' : ']]
    for pair in preprocess_list:
        code = code.replace(pair[0], pair[1])
    parser = EarleyParser(lexicon_dict, grammar_dict)
    print(code, screen_name, script_index)
    is_syn_correct = parser.parse(code.strip())
    if is_syn_correct == False:
        return {'is_valid': False}
    statement_type = getattr(parser, 'statement_type')
    tags_list = getattr(parser, 'tags_list')
    if screen_name == 'level_0' and script_index in lvl0_to_validate:
        if script_index == 4:
            is_valid = validator.validate_L0_04(statement_type, tags_list)
        elif script_index == 5:
            is_valid = validator.validate_L0_05(statement_type, tags_list)
        elif script_index == 6:
            is_valid = validator.validate_L0_06(statement_type, tags_list)
        elif script_index == 19:
            is_valid = validator.validate_L0_19(statement_type, tags_list)
        elif script_index == 20:
            is_valid = validator.validate_L0_20(statement_type, tags_list)
        elif script_index == 21:
            is_valid = validator.validate_L0_21(statement_type, tags_list)
        elif script_index == 27:
            is_valid = validator.validate_L0_27(statement_type, tags_list)
        if is_valid == False:
            return {'is_valid': False}
    elif screen_name == 'level_1' and script_index in lvl1_to_validate:
        if script_index == 4:
            is_valid = validator.validate_L1_04(statement_type, tags_list)
        elif script_index == 5:
            is_valid = validator.validate_L1_05(statement_type, tags_list)
        elif script_index == 13:
            is_valid = validator.validate_L1_13(statement_type, tags_list)
        elif script_index == 14:
            is_valid = validator.validate_L1_14(statement_type, tags_list)
        elif script_index == 20:
            is_valid = validator.validate_L1_20(statement_type, tags_list)
        if is_valid == False:
            return {'is_valid': False}
    response = {
        'is_valid': True,
        'statement_type': statement_type,
        'tags_list': tags_list,
    }
    return response