import pytest #type: ignore
from lib.diary_entry import Diary
from lib.secret_diary import SecretDiary

'''
When we create a SecretDiary instance,
An instance of Diary is created.
'''
def test_instance_of_diary_created_when_secret_diary_created():
    diary_entry = Diary('one two three')
    secret_diary = SecretDiary(diary_entry)
    assert secret_diary.diary == diary_entry

'''
When read is called on a diary instance that is locked,
Go away is returned.
'''

def test_read_method_returns_go_away_when_entry_locked():
    diary_entry = Diary('one two three')
    secret_diary = SecretDiary(diary_entry)
    with pytest.raises(Exception) as e:
        secret_diary.read()
    error_message = str(e.value)
    assert error_message == 'Go away!'

'''
When an entry is added and unlocked,
The entry contents are returned when #read method is called.
'''

def test_read_method_returns_contents_when_entry_unlocked():
    diary_entry = Diary('one two three')
    secret_diary = SecretDiary(diary_entry)
    secret_diary.unlock()
    assert secret_diary.read() == 'one two three'

'''
When an entry is added and unlocked and locked again,
An error message is returned - 'Go Away!'
'''

def test_read_method_returns_error_when_entry_unlocked_and_locked_again():
    diary_entry = Diary('one two three')
    secret_diary = SecretDiary(diary_entry)
    secret_diary.unlock()
    secret_diary.lock()
    with pytest.raises(Exception) as e:
        secret_diary.read()
    error_message = str(e.value)
    assert error_message == 'Go away!'

