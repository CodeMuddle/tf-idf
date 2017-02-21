#!/usr/bin/env python3

from utils import sentence_splitter

class DocumentError(Exception):
    def __init__(self, args):
        self.args = args

    def display(self):
        print(self.args)

class Document:
    def __init__(self, id):
        self.id = id 
        self.text = ""
        self.words = []
        self.frequency_map = {}

    def get_id(self):
        return self.id

    def load_from_file(self, filename="test.txt"):
        with open(filename, 'r') as f:
            for line in f:
                splitted = sentence_splitter(line)
                for word in splitted:
                    word_lower = word.lower()
                    self.words.append(word_lower)

    def generate_frequency_map(self):
        for word in self.words:
            count = 0
            try:
                count = self.frequency_map[word]
            except KeyError:
                count = 0
            self.frequency_map[word] = count + 1

    def get_total_term_count(self):
        return len(self.words)

    def get_word_count(self, word):
        count = 0
        try:
            count = self.frequency_map[word]
        except KeyError:
            count = 0
        return count

    
    def display(self):
        print("frequency map :\n{}".format(self.frequency_map))

def main():
    pass

if __name__ == "__main__":
    main()

