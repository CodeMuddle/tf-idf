#!/usr/bin/env python3

import re

def sentence_splitter(text):
    return re.split(r"[./?' ]+", text)


def main():
    pass

if __name__ == "__main__":
    main()

