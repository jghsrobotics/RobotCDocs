from PythonFileLibrary.HelperFunctions import *

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

    # Resets the reader's cursor to the top.
    def ResetReader(self):
        if self.canParse:
            self.currentLine = 0

    # Returns whether or not the parse has reached the end of the file.
    def ReachedEnd(self):
        return self.currentLine == len(self.lines) - 1

    # Returns the current line.
    def GetCurrentLine(self):
        if self.canParse:
            return self.lines[self.currentLine]
        return "Can't get line; File not opened."

    # View the next line without commiting.
    def PeekNextLine(self):
        nextLine = min(self.currentLine + 1, len(self.lines) - 1)
        return self.lines[nextLine]

    # Returns the next line. CleanRead() will skip ahead this line.
    def GetNextLine(self):
        if self.canParse:
            # Read next line
            self.SkipLine()
            self.currentLine = min(self.currentLine, len(self.lines) - 1)

            return self.GetCurrentLine()

        return "Can't get line; File not opened."

    # Yield function that spits out the lines of the file.
    def CleanRead(self):
        # Function that yields the next non-null line
        if self.canParse:
            yield self.GetCurrentLine()

            while not self.ReachedEnd():
                yield self.GetNextLine()
        else:
            yield "Cannot parse file"

    # Skips a number of lines (negative or positive)
    def SkipLine(self, amount = 1):
        self.currentLine += amount
