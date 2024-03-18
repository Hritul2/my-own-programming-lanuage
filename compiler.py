import re

code = '''\
ye x = 2
ye y = 2
ye sum = x ** y
bol sum
'''



def lexer(input):
    tokens = []
    cursor = 0
    while cursor < len(input):
        char = input[cursor]
        if char.isspace():
            cursor += 1
            continue
        if char.isalpha():
            word = ''
            while cursor < len(input) and input[cursor].isalnum():
                word += input[cursor]
                cursor += 1
            if word in ('ye', 'bol'):
                tokens.append({"type": 'keyword', "value": word})
            else:
                tokens.append({'type': 'identifier', 'value': word})
            continue
        if char.isdigit():
            num = ''
            while cursor < len(input) and input[cursor].isdigit():
                num += input[cursor]
                cursor += 1
            tokens.append({'type': 'number', 'value': int(num)})
            continue
        if char in ('+', '-', '*', '/', '='):
            tokens.append({'type': 'operator', 'value': char})
            cursor += 1
            continue
    return tokens

def parser(tokens):
    ast = {
        'type': 'Program',
        "body": []
    }
    
    while len(tokens) > 0:
        token = tokens.pop(0)

        if token["type"] == 'keyword' and token['value'] == 'ye':
            declaration = {
                'type': 'Declaration',
                'name': tokens.pop(0)['value'],  # Access 'value' directly
                'value': None
            }
            if tokens[0]['type'] == 'operator' and tokens[0]['value'] == '=':
                tokens.pop(0)  # Remove '=' token
                expression = ''
                # Build expression until next keyword
                while len(tokens) > 0 and tokens[0]['type'] != 'keyword':
                    expression += str(tokens.pop(0)['value'])  # Access 'value' directly
                declaration['value'] = expression.strip()  # Use strip() instead of trim()
            ast['body'].append(declaration)
        if token['type']=='keyword' and token['value']=='bol':
            ast['body'].append({'type':'Print',"expression": tokens.pop(0)['value']})
        
    return ast

def codeGen(node):
    if node['type']== 'Program':
        return '\n'.join(map(codeGen, node['body']))
    if node['type']=='Declaration':
        if node['value'] is None:
            raise ValueError(f"Variable '{node['name']}' is not assigned a value")
        return f"{node['name']}={node['value']}"
    if node['type']=='Print':
        return f"print({node['expression']})"

def compiler(input):
        tokens = lexer(input)
        ast = parser(tokens)
        executableCode = codeGen(ast)
        return executableCode


def runner(input):
    exec(input)

if __name__ == "__main__":
    execu=compiler(code)
    runner(execu)
