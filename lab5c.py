#!/usr/bin/env python3
# Author ID: afaiz-ahmad


def add(number1, number2):
    try:
        # Try converting the inputs to integers if they are strings
        number1 = int(number1)
        number2 = int(number2)
        return number1 + number2
    except ValueError:
        return 'error: could not add numbers'

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except (FileNotFoundError, PermissionError, IsADirectoryError) as e:
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10, 5))  # works
    print(add('10', 5))  # works
    print(add('abc', 5))  # exception
    print(read_file('seneca2.txt'))  # works
    print(read_file('file10000.txt'))  # exception