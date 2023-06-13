def todo_checker(string) :
    if string == '' :
        raise Exception('The string is empty, please try another string.')
    elif type(string) != str :
        raise Exception("The argument isn't a string.")
    if string.find('#TODO') != -1 :
        return True
    else : 
        return False
