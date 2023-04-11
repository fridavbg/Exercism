from functools import reduce
def wadd(x, y): return x + y
def wsub(x, y): return x - y
def wmul(x, y): return x * y
def wdiv(x, y): return x // y


validOps = {'plus': wadd,
            'minus': wsub,
            'multiplied': wmul,
            'divided': wdiv}


def curry(func, var):
    y = var

    def f(x):
        return func(x, y)
    return f


def convertToInt(lst, err):
    for x in lst:
        try:
            yield int(x)
        except:
            raise ValueError(err)


def answer(question):
    if not question.startswith('What is'):
        raise ValueError('unknown operation')
    question = question.lstrip('What is').rstrip('?')
    if question == '':
        raise ValueError('syntax error')
    tokens = [t for t in question.split(' ') if t != 'by']
    if len(tokens) == 0:
        raise ValueError('unknown operation')
    if len(tokens) == 1:
        return int(tokens[0])
    operators = [x for x in tokens
                 if tokens.index(x) % 2 == 1
                 and x in list(validOps.keys())]
    arguments = [x for x in tokens
                 if tokens.index(x) % 2 == 0]
    if (len(operators) + 1 != len(arguments)):
        raise ValueError('syntax error')
    operants = [x for x
                in convertToInt(arguments, 'syntax error')]
    try:
        curries = [curry(validOps[op], num)
                   for (op, num)
                   in zip(operators[0::1], operants[1::1])]
        if (len(curries) == 0):
            raise ValueError('unknown operation')
        if (len(curries) * 2 != len(tokens) - 1):
            raise ValueError('syntax error')
    except KeyError:
        raise ValueError('syntax error')
    return reduce(lambda num, op: op(num), curries, int(tokens[0]))

print('TEST Just 5:')
print(answer('What is 5?'))
print('TEST 5 plus 13:')
print(answer('What is 5 plus 13?'))
print('TEST 7 minus 5:')
print(answer('What is 7 minus 5?'))
print('TEST 6 multiplied by 4:')
print(answer('What is 6 multiplied by 4?'))
print('TEST 25 divided by 5:')
print(answer('What is 25 divided by 5?'))
print('TEST 5 plus 13 plus 6:')
print(answer('What is 5 plus 13 plus 6?'))
print('TEST 3 plus 2 multiplied by 3:')
print(answer('What is 3 plus 2 multiplied by 3?'))
print('TEST -3 plus 7 multiplied by -3:')
print(answer("What is -3 plus 7 multiplied by -2?"))
print('TEST invalid operator')
print(answer("What is?"))
print(answer("What is 1 plus plus 2?"))
print(answer("What is 52 cubed?"))
print('TEST syntax error')
print(answer("What is 2 2 minus 3?"))
print(answer("What is 1 plus?"))
print(answer("What is plus 1 2?"))
print(answer("What is 1 2 plus?"))
print(answer("What is -12 divided by 2 divided by -3?"))
print(answer("What is 2 multiplied by -2 multiplied by 3?"))
