# Calculate the number of anagrams of a word in a given text
# http://www.geeksforgeeks.org/anagram-substring-search-search-permutations/
#code
from collections import namedtuple
from typing import List

Data = namedtuple("Data", ["text", "word"])


def get_text() -> List[Data]:
    num_examples = input()
    examples = [] # list of tuples
    for i in range(int(num_examples)):
        examples.append(Data(text=input(), word=input()) )  # Text, Word
    return examples

def is_anagram(word, chunk):
    for char in chunk:        
        if char in word:
            word = word.replace(char, "", 1) # Remove first occurence from string 
        else:
            return False
    return True

def num_appearances(word, text):
    len_word, len_text = len(word), len(text)
    word_set = set(word)
    appearances = 0
    for i in range(len_text - len_word + 1):
        chunk = text[i: i + len_word]

        if is_anagram(word, chunk):
            appearances += 1
            
    return appearances

examples = get_text()
for data in examples:
    print(num_appearances(data.word, data.text))
