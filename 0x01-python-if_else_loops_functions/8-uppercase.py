#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        char_code = ord(str[i])
        if char_code >= 97 and char_code <= 122:
            char_code -= 32
        print(chr(char_code), end='')
    print()
