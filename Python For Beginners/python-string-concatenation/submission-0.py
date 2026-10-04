def concatenate(s1: str, s2: str) -> str:
    str1 = s1 + s2
    if len(str1) >10:
        return "Too long!"
    else:
        return str1




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
