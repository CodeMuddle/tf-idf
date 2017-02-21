#!/usr/bin/env python3

from document import Document

import math

class TFIDF:
    def __init__(self):
        self.documents = {}

    def add_document(self, document):
        self.documents[document.get_id()] = document

    def calculate_term_frequency(self, document, word):
        doc = None
        total_terms = 0
        try:
            doc = self.documents[document.get_id()]
            total_terms = document.get_total_term_count()
        except KeyError:
            print("document not found")
        word_count = doc.get_word_count(word)
        tf = word_count / total_terms
        return tf 
    
    def calculate_inverse_document_frequency(self, word):
        total_documents = len(self.documents)
        total_document_with_word = 0
        for key in self.documents:
            document = self.documents[key]
            word_count = document.get_word_count(word)
            if word_count > 0 :
                total_document_with_word += 1
        idf = 0
        if total_document_with_word > 0 and total_documents > 0:
            idf = math.log(total_documents / total_document_with_word)
        return idf 

def test():
    doc1 = Document(1)
    doc1.load_from_file("test.txt")
    doc1.generate_frequency_map()
    #doc1.display()
    #print(doc1.get_word_count('nishan'))

    doc2 = Document(2)
    doc2.load_from_file("paradox.txt")
    doc2.generate_frequency_map()
    #doc2.display()

    tfidf = TFIDF()
    tfidf.add_document(doc1)
    tfidf.add_document(doc2)

    tf = tfidf.calculate_term_frequency(doc2, "paradox")
    idf = tfidf.calculate_inverse_document_frequency("paradox")
    print("tf : {}\nidf : {}".format(tf, idf))

def main():
    test()

if __name__ == "__main__":
    main()

