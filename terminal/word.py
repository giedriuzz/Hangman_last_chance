"""Module for work with guessing word from database"""

from typing import List, Optional
from abc import ABC, abstractmethod


class Abstract(ABC):
    """class for work with get words from database"""

    @abstractmethod
    def length_of_word(self) -> int:
        """class for work with get words from database"""

    @abstractmethod
    def is_word_guessed(self) -> bool:
        """Check if a letter is in word"""

    @abstractmethod
    def is_guessed_word_equal(self) -> bool:
        """Check if a word is equal to a guess"""


class Word(Abstract):
    """class for work with get words from database"""

    not_guessed_letters_list: List[str] = []
    guessed_letters_list: List[str] = []

    def __init__(self, word: str):
        self.word = word.upper()
        self.empty_word_list = ["_" for _ in range(len(self.word))]

    def length_of_word(self) -> int:
        """Return the number of letters in the given word"""
        return len(self.word)

    def is_word_guessed(self) -> str:
        """Return guessed word for write to db"""
        alpha = "".join(self.empty_word_list)
        return alpha.isalpha()

    def is_guessed_word_equal(self) -> bool:
        """Check if a word is equal to a guess"""
        if self.word.upper() == self.word:
            return True
        return False

    def is_letter_in_not_guessed_list(self, letter: str) -> str:
        """Check is a letter is in not guessed letters list"""
        if self.not_guessed_letters_list.count(letter.upper()) >= 2:
            return False
        return True

    def is_letter_used(self, letter: str) -> bool:
        """Check is a letter is used"""
        letter_upper = letter.upper()
        if letter_upper in self.not_guessed_letters_list:
            return False
        if letter_upper in self.guessed_letters_list:
            return False
        return True

    def is_letter_in_guessed_list(self, letter: str) -> str:
        """Check is a letter is in guessed letters list"""
        if self.guessed_letters_list.count(letter.upper()) >= 2:
            return False
        return True

    def replace_guessed_letter(self, letter: str) -> list:
        """Replace a letter if it is in the word"""
        for get_letter in enumerate(self.word):
            if get_letter[1] == letter.upper():
                self.empty_word_list[get_letter[0]] = letter.upper()
            continue
        return self.empty_word_list


class Letter(Word):
    """Class for work with letters"""

    LETTERS_LIST = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]

    def __init__(self, word: str, letter: str):
        super().__init__(word)
        self.letter = letter

    def is_letter_in_word(self) -> Optional[bool]:
        """Check if a letter is in the word"""

        if self.letter in self.word:
            self.guessed_letters_list.append(self.letter)
            return True
        if self.letter not in self.word:
            self.not_guessed_letters_list.append(self.letter)
            return False
        return self.letter


if __name__ == "__main__":
    words = Word("Hello")
    letters = Letter("Hello", "G")
    print(words.length_of_word())
    print(letters.is_letter_in_word())
