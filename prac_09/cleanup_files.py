"""
CP1404/CP5632 Practical
Demos of various os module examples
"""

import os


def main():
    # """Process all subdirectories using os.walk()."""
    #
    # os.chdir('Lyrics')
    # for directory_name, subdirectories, filenames in os.walk('.'):
    #     print("Directory:", directory_name)
    #     print("\tcontains subdirectories:", subdirectories)
    #     print("\tand files:", filenames)
    #     print("(Current working directory is: {})".format(os.getcwd()))
    #
    #     for filename in filenames:
    #         filename_with_path = os.path.join(directory_name, filename)
    #         new_filename_with_path = os.path.join(directory_name, get_fixed_filename(filename))
    #         os.rename(filename_with_path, new_filename_with_path)

    # Tests for get_fixed_filename:
    filename = "Away In A MangerNoCrib for (a bed).TXT"
    print(filename)
    print(get_fixed_filename(filename))


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    name_without_spaces = filename.replace(" ", "_")
    name_with_correct_extension = name_without_spaces.replace(".TXT", ".txt")
    fixed_name = ""
    fixed_letter = ""

    for i, letter in enumerate(name_with_correct_extension):
        try:
            if letter.islower() and name_with_correct_extension[i + 1].isupper():
                print("fix PascalCase")
                fixed_letters = letter + "_"
                fixed_name += fixed_letters
            else:
                fixed_name += letter
        except IndexError:
            fixed_name += letter

    return fixed_name


main()
