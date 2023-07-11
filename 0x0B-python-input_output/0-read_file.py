#!/usr/bin/python3
"""Module to read a file"""



def read_file(filename=""):
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
