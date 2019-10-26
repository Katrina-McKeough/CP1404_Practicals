"""
CP1404/CP5632 Practical 9
"""

import shutil
import os


def main():
    """ Create a directory for groups of file extensions and sort files into directories from user input. """
    extensions_to_categories = {}
    os.chdir('FilesToSort')
    print('Directory:', os.getcwd())
    print('Contains files:', os.listdir('.'))
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        print('Moving ' + filename)
        file_extension = filename[filename.find(".") + 1:]
        if file_extension not in extensions_to_categories:
            new_category = input("What category would you like to sort {} files into? ".format(file_extension))
            extensions_to_categories[file_extension] = new_category
            try:
                os.mkdir(new_category)
            except FileExistsError:
                pass
        shutil.move(filename, extensions_to_categories[file_extension] + '/' + filename)


main()
