# As a user
# So that I can manage my time
# # I want to see an estimate of reading time for a text,
#  assuming that I can read 200 words a minute.

# A function
# def estimate_reading_time(text):
# parameters:
# takes text

# returns:
#  reading time of text given 200wpm
# formatted number
# rounded up

# side effects:
# throws exception for non-text argument

def estimate_reading_time(text):
    if type(text) != str :
        raise Exception("Argument not in string format!")
    split_words = text.split()
    number_of_words = len(split_words)
    time_estimate = f"{round(number_of_words/200)} mins"
    return time_estimate