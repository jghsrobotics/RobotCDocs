from FileScanner import *
import os

"""
    RecursiveScanner.py

    Recursively scans a root directory for leaf nodes and
    creates a FileScanner object for each of them.
"""
class RecursiveScanner:
    def __init__(self, settingParser):
        self.files = []
        self.whitelist = ['.c', '.h']
        self.Scan(settingParser.libraryDirectory)

    def Scan(self, directory):
        for obj in os.listdir(directory):
            # If it's a folder, keep searching.
            if '.' not in obj:
                self.Scan(os.path.join(directory, obj))

            else:
                # If it's a file in our whitelist, make a FileScanner for it
                for item in self.whitelist:
                    if item in obj:
                        self.files.append(FileScanner(os.path.join(directory, obj)))
