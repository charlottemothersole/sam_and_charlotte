# test count words takes a string
from lib.count_words import *
import pytest 

def test_count_words_takes_string():
    result = count_words('type')
    assert result == 1

# test count words returns number of words in the string 
def test_count_words_returns_wordcount():
    result = count_words('a small string')
    assert result == 3
# test count words return exception for non string type argument

def test_count_words_exception_non_string_type():
    with pytest.raises(Exception) as e:
        count_words(321334142)
    error_message = str(e.value)
    assert error_message == 'no numbers in my domain'
    
#  test for empty string

def test_count_words_takes_empty_string():
    result = count_words('')
    assert result == 0

def test_count_words_takes_long_list_spaces():
    result = count_words('               ')
    assert result == 0
