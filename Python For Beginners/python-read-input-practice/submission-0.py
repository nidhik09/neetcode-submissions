def add_two_numbers() -> int:
    ip = input()
    strings = ip.split(",")
    l1 = []
    for i in strings:
        l1.append(int(i))
    return sum(l1)



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
