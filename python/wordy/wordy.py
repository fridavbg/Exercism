def extract_numbers_and_operators(s):
    current_number = ''
    numbers = []
    operators = []
    operator_words = ['plus', 'minus', 'multiplied', 'divided']
    for word in s[:-1].split():
        if word.isdigit() or (word[0] == '-' and word[1:].isdigit()):
            numbers.append(int(word))
        elif word in operator_words:
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

    numbers_operators = extract_numbers_and_operators(question)
    numbers = numbers_operators[0]
    operators = numbers_operators[1]
    if len(numbers) == 0 and len(operators) == 0:
        raise ValueError("unknown operation")
    result = numbers_operators[0][0]
    operator_words = ['plus', 'minus', 'multiplied', 'divided']

    if len(numbers) == 1 and len(operators) == 0 and len(question) <= 10:
        return result

    if len(operators) == 1 and len(numbers) == 1:
        raise ValueError("syntax error")
    elif len(operators) == len(numbers):
        raise ValueError("syntax error")
    elif len(operators) == 1 and len(numbers) > 2:
        raise ValueError("syntax error")
    elif len(numbers) >= 2 and len(operators) < 1:
        raise ValueError("syntax error")
    elif len(numbers) == 2 and len(operators) == 2:
        raise ValueError("syntax error")
    if len(numbers) <= 2 and len(operators) > 0:
        if operators[0] == 'plus':
            result += numbers[1]
        elif operators[0] == 'minus':
            result -= numbers[1]
        elif operators[0] == 'multiplied':
            result *= numbers[1]
        elif operators[0] == 'divided':
            result = int(result / numbers[1])
        return result
    elif len(numbers) == 3:
        if operators[0] == 'plus':
            result += numbers[1]
        elif operators[0] == 'minus':
            result -= numbers[1]
        elif operators[0] == 'multiplied':
            result *= numbers[1]
        elif operators[0] == 'divided':
            result = int(result / numbers[1])

        if operators[1] == 'plus':
            result += numbers[2]
        elif operators[1] == 'minus':
            result -= numbers[2]
        elif operators[1] == 'multiplied':
            result *= numbers[2]
        elif operators[1] == 'divided':
            print('HERE')
            print(result / numbers[2])
            result = result / numbers[2]
        return int(result)
    else:
        raise ValueError("unknown operation")


# print('TEST Just 5:')
# print(answer('What is 5?'))
# print('TEST 5 plus 13:')
# print(answer('What is 5 plus 13?'))
# print('TEST 7 minus 5:')
# print(answer('What is 7 minus 5?'))
# print('TEST 6 multiplied by 4:')
# print(answer('What is 6 multiplied by 4?'))
# print('TEST 25 divided by 5:')
# print(answer('What is 25 divided by 5?'))
# print('TEST 5 plus 13 plus 6:')
# print(answer('What is 5 plus 13 plus 6?'))
# print('TEST 3 plus 2 multiplied by 3:')
# print(answer('What is 3 plus 2 multiplied by 3?'))
# print('TEST -3 plus 7 multiplied by -3:')
# print(answer("What is -3 plus 7 multiplied by -2?"))
# print('TEST invalid operator')
# print( answer("What is?"))
# print(answer("What is 1 plus plus 2?"))
# print(answer("What is 52 cubed?"))
# print('TEST syntax error')
# print(answer("What is 2 2 minus 3?"))
# print(answer("What is 1 plus?"))
# print(answer("What is plus 1 2?"))
# print(answer("What is 1 2 plus?"))
# print(answer("What is -12 divided by 2 divided by -3?"))
# print(answer("What is 2 multiplied by -2 multiplied by 3?"))
