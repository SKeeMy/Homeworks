from typing import List
import string
from collections import Counter
from collections import Counter


def get_longest_diverse_words(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        text = file.read()
        words = text.split()
        word_set = [(w,set(w)) for w in words]
        sorted_word_set = sorted(word_set, key=lambda x: (-len(x[1]), -len(x[0])))
        return [w[0] for w in sorted_word_set[:10]]


def get_rarest_char(file_path: str) -> str:
    with open(file_path, 'r') as file:
        text = file.read()
        counter = Counter(filter(lambda x: x not in string.whitespace, text))
        rarest = min(counter.items(), key=lambda x: x[1])
        return rarest[0]

def count_punctuation_chars(file_path: str) -> int:
    with open(file_path, 'r') as file:
        text = file.read()
        return sum(1 for c in text if c in string.punctuation)

def count_non_ascii_chars(file_path: str) -> int:
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        return sum(1 for c in text if ord(c) > 127 and c not in string.whitespace)



def get_most_common_non_ascii_char(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        counter = Counter(filter(lambda c: ord(c) > 127 and c not in string.whitespace, text))
        return counter.most_common(1)[0][0]