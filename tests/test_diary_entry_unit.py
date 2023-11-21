from lib.diary_entry import *
from unittest.mock import Mock

'''
Given I initialise a diary
It has a contents parameter that is a string
'''
def test_diary_has_contents_as_string():
    diary_entry = Diary('one two three')
    assert diary_entry.contents == 'one two three'

'''
Given I initialise a diary with contents
I can call read to return the contents
'''
def test_read_diary():
    diary_entry = Diary('one two three')
    assert diary_entry.read() == 'one two three'