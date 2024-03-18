import re

code= '''\
ye x = 10
ye y = 20
ye sum = x + y
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
            # Check for assignment
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


def compiler(input):
    tokens= lexer(input)
    ast=parser(tokens)
    executableCode=codeGen(ast)
    for i in ast['body']:
        print(i)



if __name__ == "__main__":
    compiler(code)