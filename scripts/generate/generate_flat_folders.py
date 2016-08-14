#!/usr/bin/env python
# or execute with py -3 generate_flat_folders.py

import random, os

# todo: separate console interaction from the generation of flat folders

def single_level_folders(path, amount, name_len):
    """
    Generate #amount of folders in the path location.
    If such folder already exists, it is skipped.
    Thus less folders then requested could actually be generated (altough this is unlikely for reasonable name_len's).

    name_len is the length of each folder.
    Each folder name is a random string of the characters "A", "B", "C", "D", "E", "F" and
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9".

    """
    for i in range(amount):
        p = os.path.join(path, random_text(name_len))
        create_dir_ifn_exist(p)


def create_dir_ifn_exist(folder_path):
    """
    Creates a folder at the folder_path if the path does not yet exist.

    Note:
    A race condition can exist if a folder is created externally between the if statement below
    and the os.makedirs() function execution.
    """
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def random_text(length, chars="0123456789ABCDEF"):
    """
    Generates a string of random characters of the given 'length'.

    The characters used for the string are those defined as 'chars'.
    """

    word = []
    for i in range(length):
        word.append(random.choice(chars))

    return "".join(word)

def request_path(label="path"):
    """
    Requests input from the user until the stop condition is reached.

    This particular function requests a path.
    """
    inp = input("{req}> ".format(req=label))

    if os.path.isdir(inp):
        return inp
    else:
        print(os.path.exists(inp))
        return request_path()

def request_decimal_input(label="amount"):
    """
    Requests input from the user until the stop condition is reached.

    This particular function requests a single decimal number.
    """

    inp = input("{req}> ".format(req=label))

    if inp.isdecimal():
        return int(inp)
    else:
        return request_decimal_input()


def request_yesno(label="mult_folders"):
    """
    Requests input from the user until the stop condition is reached.

    This particular function requests a yes or no, which are returned as True and False respectively.
    """

    inp = input("{req} (y/n)> ".format(req=label))
    inp = inp.strip().lower()

    if inp == "y":
        return True
    elif inp == "n":
        return False
    else:
        request_yesno()

if __name__ == '__main__':
    single_level_folders(request_path(), request_decimal_input(), request_decimal_input(label="folder name length"))
