import re

code= '''\
ye x = 10
ye y = 20
ye sum = x + y
bol sum
'''


def lexer(input):
    tokens=[]
    cursor=0
    while cursor< len(input):
        char=input[cursor]
        # skip if white space
        if re.match(r'\s', char):
            cursor+=1
            continue
        # fill word for characters
        if re.search(r'[a-zA-Z]', char):
            word=''
            while cursor < len(input) and re.search(r'[a-zA-Z]', char):
                word+=char
                cursor+=1
                if cursor < len(input):
                    char = input[cursor]
            
            if word in ('ye', 'bol'):
                tokens.append({"type":'keyword',"value":word})
            else:
                tokens.append({'type':'identifier','value':word})
            
            continue
        # Fill num for numerals
        if re.search(r'[0-9]', char):
            num=''
            while cursor < len(input) and re.search(r'[0-9]', char):
                num+=char
                cursor+=1
                char=input[cursor]
            tokens.append({'type':'number', 'value':int(num)})
            continue
        # For operators and assignment operator
        if re.search(r'[\+\-\*\/=]', char):
            tokens.append({'type': 'operator', 'value': char})
            cursor += 1
            continue
    return tokens




def compiler(input):
    tokens= lenxer(input)



if __name__ == "__main__":
    tokens = lexer(code)
    for token in tokens:
        print(token)