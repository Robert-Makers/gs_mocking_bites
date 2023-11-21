class SecretDiary:
    def __init__(self, diary):
        self.diary = diary
        self.locked = True
        pass

    def read(self):
        # Raises the error "Go away!" if the diary is locked
        # Returns the diary's contents if the diary is unlocked
        # The diary starts off locked
        if self.locked == True:
            raise Exception('Go away!')
        else:
            '''
            return self.diary.contents
            return self.diary.read()
            '''
            return self.diary.contents

    def lock(self):
        # Locks the diary
        # Returns nothing
        self.locked = True

    def unlock(self):
        # Unlocks the diary
        # Returns nothing
        self.locked = False