"""
This function takes the name of a directory
and prints out the paths files within that
directory as well as any files contained in
contained directories.

This function is similar to os.walk. Please don't
use os.walk in your answer. We are interested in your
ability to work with nested structures.
"""

import os

def print_directory_contents(sPath):
    for direc in os.listdir(sPath):
        path = os.path.join(sPath, direc)
        if os.path.isdir(path):
            print_directory_contents(path)
        else:
            print(path)


print_directory_contents('/Users/emila/Desktop/codewars')