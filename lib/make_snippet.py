# Design

def make_snippet(string):
    word_list = string.split()
    if len(word_list) == 0:
        raise Exception('give me a string!')
    elif len(word_list) >= 6:
        first_five_words = word_list[0:5]
        word_string = ' '.join(first_five_words)
        return word_string+'...'
    else:
        return string
# A function called make_snippet that takes a string as an argumen
# t and returns the first five words and then a '...' if there are more than that.