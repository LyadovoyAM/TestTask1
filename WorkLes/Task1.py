import pprint
from collections import Counter

with open('text_for_count.txt', 'r') as text:
    text_for_count = text.read()
    symbols_count = Counter(text_for_count)
    pprint.pprint(symbols_count)
