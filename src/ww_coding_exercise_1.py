#!/usr/bin/env python3
import sys


def does_file_exists(path):
    try:
        f = open(path, "r")
        f.close()
        return True
    except Exception as e:
        print(e)


def read_from_file(path):
    f = open(path, "r")
    text = f.read()
    f.close()
    return text


def get_dictionary(text):
    lines = text.splitlines()
    dictionary = {}
    for line in lines:
        split_line = line.split(" – ")
        dictionary[split_line[0]] = split_line[1].split(",")
    return dictionary


def print_dictionary(dictionary):
    for k, v in dictionary.items():
        print(k)
        for item in v:
            print(item.strip())


def main(path):
    if does_file_exists(path):
        text = read_from_file(path)
        dictionary = get_dictionary(text)
        print_dictionary(dictionary)


if __name__ == "__main__":
    main(str(sys.argv[1]))

# main("../tst/resources/input.txt")


