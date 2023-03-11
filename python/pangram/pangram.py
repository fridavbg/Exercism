alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def is_pangram(sentence):
    sentence = sentence.lower()
    has_all = all([char in sentence for char in alphabet])
    return has_all

print(is_pangram('"Five quacking Zephyrs jolt my wax bed."'))