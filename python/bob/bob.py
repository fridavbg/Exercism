def response(hey_bob):
    hey_bob =  hey_bob.strip()
    if hey_bob.isspace() or not hey_bob:
        return 'Fine. Be that way!'
    elif hey_bob[-1] == '?':
        if hey_bob.isupper():
            return "Calm down, I know what I'm doing!"
        else:
            return 'Sure.'
    elif hey_bob.isupper():
        return 'Whoa, chill out!'
    else:
        return 'Whatever.'

# Whatever.
print(1, response("Tom-ay-to, tom-aaaah-to.")) 
# Whoa, chill out!
print(2, response("WATCH OUT!"))
# Whoa, chill out!
print(3, response("FCECDFCAAB"))
# Sure.
print(4, response("Does this cryogenic chamber make me look fat?"))
# Sure.
print(5, response("Okay if like my  spacebar  quite a bit?   "))
# Whoa, chill out!
print(6, response("1, 2, 3 GO!"))
# Fine. Be that way!
print(7, response("          "))
# Calm down, I know what I'm doing!
print(8, response("WHAT'S GOING ON?"))
# Whoa, chill out!
print(9, response("I HATE THE DENTIST"))
# Fine. Be that way!
print(10, response("\n\r \t"))
# Whatever
print(11, response("         hmmmmmmm..."))