def remove_fourth_character(word: str) -> str:
    before_str = word[:3]
    after_str = word[4:]
    final = before_str + after_str
    return final

# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
