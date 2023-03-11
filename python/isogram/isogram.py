def is_isogram(string):
    dict = {}
    sp_chars = [' ', '-']
    res = True
    for sp_char in sp_chars:
        if sp_char in string:
            string = string.replace(sp_char, '')
    for letter in string.lower():
        dict[letter] = dict.get(letter,0)+1
    for count in dict.values():
        if count > 1:
            res = False
    return res
