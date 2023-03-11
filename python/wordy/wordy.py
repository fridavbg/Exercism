def answer(question):
    arr_words = question[:len(question)-1].split()
    if len(arr_words) == 3:
        return arr_words[2]
    for i, word in enumerate(arr_words):
        if len(arr_words) < 7:
            if arr_words[3] == "plus":
                return int(arr_words[2]) + int(arr_words[4])
            elif arr_words[3] == "minus":
                return int(arr_words[2]) - int(arr_words[4])
            elif arr_words[3] == "multiplied":
                return int(arr_words[2]) * int(arr_words[5])
            elif arr_words[3] == "divided":
                return round(int(arr_words[2]) / int(arr_words[5]))
        else:
            if arr_words[3] == "plus" and arr_words[5] == "plus":
                return int(arr_words[2]) + int(arr_words[4]) + int(arr_words[6])
            if arr_words[3] == "plus" and arr_words[5] == "minus":
                return int(arr_words[2]) + int(arr_words[4]) - int(arr_words[6])
            if arr_words[3] == "minus" and arr_words[5] == "minus":
                return int(arr_words[2]) - int(arr_words[4]) - int(arr_words[6])
            if arr_words[3] == "minus" and arr_words[5] == "plus":
                    return int(arr_words[2]) - int(arr_words[4]) + int(arr_words[6])

# print(answer("What is 5?"))
# print(answer("What is 1 plus 1?"))
# print(answer("What is 53 plus 2?"))
# print(answer("What is -1 plus -10?"))
# print(answer("What is 123 plus 45678?"))
# print(answer("What is 4 minus -12?"))
# print(answer("What is -3 multiplied by 25?"))
# print(answer("What is 33 divided by -3?"))
# print(answer("What is 1 plus 1 plus 1?"))
# print(answer("What is 1 plus 5 minus -2?"))
# print(answer("What is 20 minus 4 minus 13?"))
# print(answer("What is 17 minus 6 plus 3?"))
print(answer("What is 2 multiplied by -2 multiplied by 3?"))