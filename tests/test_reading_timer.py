from lib.reading_timer import *
import pytest
# test takes empty string returns zero
# test takes string returns formatted string length/200 for input that will round up
# test takes string returns formatted string length/200 for input that will round down
# test makes exception for non-text

def test_reading_timer_empty_string() :
    result = estimate_reading_time('')
    assert result == "0 mins"

def test_reading_timer_round_up() :
    result = estimate_reading_time("This string should take 1 minute roughly to fully read This string should take 1 minute roughly to fully read This string should take 1 minute roughly to fully read This string should take 1 minute roughly to fully read This string should take 1 minute roughly to fully read This string should take 1 minute roughly to fully read This string should take 1 minute roughly to fully read This string should take 1 minute roughly to fully read This string should take 1 minute roughly to fully read This string should take 1 minute roughly to fully read This string should take 1 minute roughly to fully read")
    assert result == "1 mins"

def test_reading_timer_round_down() :
    result = estimate_reading_time("This should round down")
    assert result == "0 mins"

def test_reading_timer_exception() :
    with pytest.raises(Exception) as e:
        estimate_reading_time(12345)
    error_message = str(e.value)
    assert error_message == "Argument not in string format!"
