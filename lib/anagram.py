# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.anagrams = []

    def match(self, words):
        for word in words:
            if self.is_anagram(word):
                self.anagrams.append(word)
        return self.anagrams

    def is_anagram(self, word):
        return sorted(self.word) == sorted(word.lower())