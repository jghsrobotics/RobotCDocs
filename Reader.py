from HelperFunctions import *

"""
    Reader.py

    Reads a file!
"""
class Reader:
    def __init__(self, fileName):
        self.fileName = fileName
        self.file = OpenFileSafely(fileName, "r", True)
        self.canParse = self.file is not None

        if self.canParse:
            self.lines = self.file.readlines()
            self.currentLine = 0

    # Returns whether or not the parse has reached the end of the file.
    def ReachedEnd(self):
        return self.currentLine == len(self.lines) - 1

    # Returns the stripped string of the current line.
    def GetCurrentLine(self):
        return self.lines[self.currentLine].strip()

    # Returns the next line by skipping spaces.
    def GetNextLine(self):
        # Read next non-null lines
        self.currentLine += 1
        self.currentLine = min(self.currentLine, len(self.lines) - 1)

        while len(self.GetCurrentLine()) == 0 and not self.ReachedEnd():
            self.currentLine += 1

        return self.GetCurrentLine()
