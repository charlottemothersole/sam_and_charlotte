
# Write a small example as a test.
from lib.make_snippet import *
import pytest

def test_make_snippet_takes_string():
    result = make_snippet('a quick brown fox jumped')
    assert result == 'a quick brown fox jumped'

# check longer string only returns first five words
def test_make_snippet_returns_five_of_long_string_with_ellipsis():
    result = make_snippet('a quick brown fox jumped over the lazy dog')
    assert result == 'a quick brown fox jumped...'


def test_make_snippet_if_string_empty():
    with pytest.raises(Exception) as e:
        make_snippet('')
    assert str(e.value) == 'give me a string!'


# Run the test (RED).
# Write enough code to make that test pass.
# Run the test (GREEN).
# Refactor if necessary.
# Return to step 1 and keep going until your program is complete.
