from lib.grammar_checker import *
import pytest

def test_grammar_checker_empty_string() :
    with pytest.raises(Exception) as e:
        grammar_checker('')
    error_message = str(e.value)
    assert error_message == 'The string is empty, please try another string.'

def test_grammar_checker_correct_string() :
    result = grammar_checker('This is a good string!')
    assert result == 'Great grammar!'

def test_grammar_checker_wrong_string() :
    result = grammar_checker('this string sucks')
    assert result == "Sorry, this string doesnt end with ./!/?"

def test_grammar_checker_capital() :
    result = grammar_checker('this string is average.')
    assert result == "Sorry, this string doesn't start with a capital letter."