#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value=''):
        if not isinstance(value, str):
            print("The value must be a string.")
            self.value = ''
        else:
            self.value = value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        # Use regular expression to split the string into sentences
        sentences = re.split(r'[.!?]', self.value)
        # Count the number of non-empty sentences
        count = sum(1 for sentence in sentences if sentence.strip())
        return count