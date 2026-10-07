from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    char_count = {}
    count = 0
    for char in word:
        count = 0
        if char not in char_count:
            for c in word:
                if c == char:
                 count+= 1
            char_count[char] = count
    return char_count
# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
