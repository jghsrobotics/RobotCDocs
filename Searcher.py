import os
from Scanner import *

"""
    Searcher.py

    Traverses a root directory to scan all RobotC files.
"""
class Searcher:
    def __init__(self, rootDirectory):
        self.rootDirectory = rootDirectory

    def ListRobotCFiles(self, directory):
        files = os.listdir(directory)

        robotC = []

        for file in files:
            # Recursively search .h files
            if '.' not in file:
                robotC.extend(self.ListRobotCFiles(directory + "\\" + file))

            elif '.h' in file:
                robotC.append(directory + "\\" + file)

        return robotC