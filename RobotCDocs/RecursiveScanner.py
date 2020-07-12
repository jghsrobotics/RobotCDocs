import PythonFileLibrary.RecursiveScanner
from FileScanner import *

"""
    RecursiveScanner.py

    Recursively scans a root directory for leaf nodes and
    creates a FileScanner object for each of them.
"""
class RecursiveScanner(PythonFileLibrary.RecursiveScanner.RecursiveScanner):
    def __init__(self, settingParser):
        super().__init__(settingParser.libraryDirectory, ['.c', '.h'])
        self.scanners = [];

        self.ParseFiles()

    def ParseFiles(self):
        for path in self.files:
            # If it's a folder, keep searching.
            self.scanners.append(FileScanner(path))
