from lib.todo_checker import *
import pytest

def test_todo_checker_empty_string() :
    with pytest.raises(Exception) as e:
        todo_checker('')
    error_message = str(e.value)
    assert error_message == 'The string is empty, please try another string.'

def test_todo_checker_non_string() :
    with pytest.raises(Exception) as e:
        todo_checker(1234)
    error_message = str(e.value)
    assert error_message == "The argument isn't a string."

def test_todo_checker_correct_string() :
    result = todo_checker('This string includes #TODO')
    assert result == True

def test_todo_checker_incorrect_string() :
    result = todo_checker('This string doesnt')
    assert result == False