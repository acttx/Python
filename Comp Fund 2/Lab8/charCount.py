from comparable import Comparable


class CharCount(Comparable):

    def __init__(self, char, count):
        self.char = char
        self.count = count

    def get_char(self):
        return self.char

    def get_count(self):
        return self.count

    def compare(self, other_charCount):
        if self.char < other_charCount.char:
            return -1

        if self.char > other_charCount.char:
            return 1

        return 0

    def __str__(self):
        return str(self.char) + " : " + str(self.count)
