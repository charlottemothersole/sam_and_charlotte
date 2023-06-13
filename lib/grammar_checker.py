def grammar_checker(string) :
    if string == '' :
        raise Exception('The string is empty, please try another string.')
    elif(string[-1] not in ['.','!','?']) :
        return 'Sorry, this string doesnt end with ./!/?'
    elif(not string[0].isupper()) :
        return "Sorry, this string doesn't start with a capital letter."
    else :
        return 'Great grammar!'