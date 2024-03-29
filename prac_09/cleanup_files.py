"""
CP1404/CP5632 Practical
Demos of various os module examples
"""

import os


def main():
    """Process all subdirectories using os.walk()."""

    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            filename_with_path = os.path.join(directory_name, filename)
            new_filename_with_path = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(filename_with_path, new_filename_with_path)

    # Tests for get_fixed_filename:
    # filename = "Away In A MangerNoCrib for (a bed) ICan'tTest.TXT"
    # print(filename)
    # print(get_fixed_filename(filename))


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    name_without_spaces = filename.replace(" ", "_")
    fixed_name = ""
    fixed_letters = ""

    for i, letter in enumerate(name_without_spaces):
        try:
            if letter.islower() and name_without_spaces[i + 1].isupper():
                fixed_letters = letter + "_"
            elif letter.isupper() and name_without_spaces[i + 1].isupper() and name_without_spaces[i + 2].islower():
                fixed_letters = letter + "_"
            elif letter.islower() and not name_without_spaces[i - 1].isalpha() and not name_without_spaces[
                                                                                           i - 1] == "'":
                fixed_letters = letter.capitalize()
            else:
                fixed_letters = letter
        except IndexError:
            pass
        fixed_name += fixed_letters
    fixed_name_with_extension = fixed_name.replace(fixed_name[fixed_name.find("."):], ".txt")
    return fixed_name_with_extension


main()
