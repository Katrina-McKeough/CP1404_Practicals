"""
CP1404/CP5632 Practical 9
"""

import shutil
import os


def main():
    """ Create a directory for each file extension and sort files into corresponding directories. """

    os.chdir('FilesToSort')
    print('Directory:', os.getcwd())
    print('Contains files:', os.listdir('.'))
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        print('Moving ' + filename)
        file_extension = filename[filename.find(".") + 1:]
        try:
            os.mkdir(file_extension)
        except FileExistsError:
            pass
        shutil.move(filename, file_extension + '/' + filename)


main()
