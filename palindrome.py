class Palindrome:
    def __init__(self, word):
        self.word = word

    def reversed_word(self):
        my_original_word = self.word.lower()
        my_reversed_word = my_original_word[::-1]

        if my_reversed_word == my_original_word:
            return True
        else:
            return False