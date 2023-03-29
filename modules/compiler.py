import random
random.seed(9999)

id_list = list(range(10000, 99999))

lexicon_dict = {
    'int': ['int'],
    'var_name': ['x', 'y', 'my_var'],
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
    'statement': [['assignment'], ['conditional'], ['loop']],
    'assignment': [['int_ass']],
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
}

class EarleyRow:
    def __init__(self, pid, chart, operator, start, end, symbol, production):
        eid = id_list[random.randint(0, len(id_list) - 1)]
        id_list.remove(eid)
        self.eid = eid
        self.pid = pid
        self.chart = chart
        self.operator = operator
        self.start = start
        self.end = end
        self.symbol = symbol
        self.production = production
    
    def print_row(self):
        print(self.chart, self.eid, self.pid, self.operator, self.start, self.end, self.symbol, self.production)

class EarleyParser:
    def __init__(self, lexicon, grammar):
        self.lexicon = lexicon
        self.grammar = grammar
        self.terminals = [key for key in lexicon]
        self.nonterminals = [key for key in grammar]

    def shift_dot(self, prod):
        if '*' in prod:
            index = prod.index('*')
            prod.remove('*')
            prod.insert(index + 1, '*')
            return prod

    def predict(self, earley_row):
        prod = getattr(earley_row, 'production')
        for child_prod in self.grammar[prod[prod.index('*') + 1]]:
            pid = getattr(earley_row, 'eid')
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
            pid = getattr(earley_row, 'eid')
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
            pid = getattr(to_comp_row, 'pid')
            chart = getattr(comp_row, 'chart')
            start = getattr(comp_row, 'start')
            end = getattr(comp_row, 'end')
            symbol = getattr(to_comp_row, 'symbol')
            prod = getattr(to_comp_row, 'production').copy()
            comp_row = EarleyRow(pid, chart, 'COMP', start, end, symbol, self.shift_dot(prod))
            self.table.append(comp_row)
            comp_symbol = getattr(comp_row, 'symbol')
            comp_prod = getattr(comp_row, 'production')
            to_comp_row = ([row for row in self.table if row.eid == pid])[0]
            
    
    def parse(self, sentence):
        sentence = sentence.split()
        self.table = [EarleyRow(999, 0, 'PRED', 0, 0, 'y', ['*', 'S'])]
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
        global id_list
        id_list = list(range(10000, 99999))
        if getattr(self.table[-1], 'symbol') == 'S' and getattr(self.table[-1], 'production')[-1] == '*':
            return True
        return False
    
# parser = EarleyParser(lexicon_dict, grammar_dict)
# print(parser.parse('int my_int = 0 ;'))