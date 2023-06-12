# Design

# A function called count_words that takes a string
def count_words(string):
    if type(string) != str:
        raise Exception('no numbers in my domain')
    the_list = string.split()
    return len(the_list)

# as an argument and returns the number of words in that string.