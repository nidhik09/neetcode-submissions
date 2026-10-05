def reverse_string(input_string: str) -> str:
    length = len(input_string) - 1
    return input_string[length::-1]
# do not modify below this line
print(reverse_string("NeetCode"))
print(reverse_string("Hello!"))
print(reverse_string("Bye Bye"))
