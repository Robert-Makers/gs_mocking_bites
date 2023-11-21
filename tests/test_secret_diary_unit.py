from unittest.mock import Mock
from lib.secret_diary import SecretDiary
import pytest #type: ignore

'''
Given I initialise a SecretDiary
It has a locked property set to True
It has a diary property
'''
def test_secret_diary_has_locked_property():
    fake_diary_entry = Mock()
    secret_diary = SecretDiary(fake_diary_entry)
    assert secret_diary.locked == True
    assert secret_diary.diary == fake_diary_entry

'''
If I try to read the secret diary
Return Go away as an error
'''
def test_secret_diary_locked_by_default():
    fake_diary_entry = Mock()
    secret_diary = SecretDiary(fake_diary_entry)
    with pytest.raises(Exception) as e:
        secret_diary.read()
    error_message = str(e.value)
    assert error_message == 'Go away!'

'''
If I try to read the secret diary after it is unlocked
Return the diary contents
'''
def test_secret_diary_is_unlocked():
    fake_diary_entry = Mock()
    fake_diary_entry.contents = 'one two three'
    # fake_diary_entry.read.return_value = 'one two three
    secret_diary = SecretDiary(fake_diary_entry)
    secret_diary.unlock()
    assert secret_diary.read() == fake_diary_entry.contents # fake_diary_entry.read()

'''
If I create a diary, unlock it then lock it again
Return go away error
'''
def test_unlock_then_re_lock_secret_diary():
    fake_diary_entry = Mock()
    fake_diary_entry.contents = 'one two three'
    # fake_diary_entry.read.return_value = 'one two three
    secret_diary = SecretDiary(fake_diary_entry)
    secret_diary.unlock()
    secret_diary.lock()
    with pytest.raises(Exception) as e:
        secret_diary.read()
    error_message = str(e.value)
    assert error_message == 'Go away!'