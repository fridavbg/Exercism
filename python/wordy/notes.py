OPERATOR_WORDS = ['plus', 'minus', 'multiplied', 'divided']

def apply_operator(operator, num1, num2):
    if operator == 'plus':
        return num1 + num2
    elif operator == 'minus':
        return num1 - num2
    elif operator == 'multiplied':
        return num1 * num2
    elif operator == 'divided':
        return num1 // num2

def extract_numbers_and_operators(s):
    current_number = ''
    numbers = []
    operators = []
    for word in s[:-1].split():
        if word.isdigit() or (word[0] == '-' and word[1:].isdigit()):
            numbers.append(int(word))
        elif word in OPERATOR_WORDS:
            operators.append(word)
            if current_number:
                numbers.append(int(current_number))
                current_number = ''
        else:
            if current_number:
                numbers.append(int(current_number))
                current_number = ''
    if current_number:
        numbers.append(int(current_number))
    if not operators and numbers:
        return numbers, operators
    return numbers, operators

def answer(question):
    if question == 'What is?':
        raise ValueError('syntax error')

    previous_token_was_number = False
    for token in question[:-1].split():
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            if previous_token_was_number:
                raise ValueError('syntax error')
            previous_token_was_number = True
        else:
            previous_token_was_number = False

    numbers, operators = extract_numbers_and_operators(question)
    if len(numbers) == 0 and len(operators) == 0:
        raise ValueError("unknown operation")
    
    result = numbers[0]
    if len(numbers) == 1 and len(operators) == 0 and len(question) <= 10:
        return result

    for i in range(len(operators)):
        if len(operators) == len(numbers) - 1:
            result = apply_operator(operators[i], result, numbers[i+1])
        else:
            raise ValueError('syntax error')

    return result


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
print( answer("What is?"))
print(answer("What is 1 plus plus 2?"))
print(answer("What is 52 cubed?"))
print('TEST syntax error')
print(answer("What is 2 2 minus 3?"))
print(answer("What is 1 plus?"))
print(answer("What is plus 1 2?"))
print(answer("What is 1 2 plus?"))
print(answer("What is -12 divided by 2 divided by -3?"))
print(answer("What is 2 multiplied by -2 multiplied by 3?"))
