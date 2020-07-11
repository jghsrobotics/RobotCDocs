from PythonFileLibrary.Reader import *

"""
    SettingParser.py

    Parses setup.txt.
"""
class SettingParser(Reader):
    def __init__(self):
        super().__init__("setup.txt")
        self.libraryName = ""
        self.libraryDirectory = ""
        self.outputDirectory = ""

        try:
            self.Parse()
        except AssertionError as error:
            print(error)

    # Yield lines that have '>' in them. The file
    # can still be read normally using self.GetNextLine()
    # or self.SkipLine(n)
    def GetSettings(self):
        for line in self.CleanRead():
            if '>' in line:
                yield line.strip()

    # Parse setup.txt. Will throw an AssertionError if the
    # file cannot be read.
    def Parse(self):
        assert self.canParse, "SettingParser.py: Could not parse setup.txt."

        currentSetting = 0
        for line in self.GetSettings():
            currentSetting += 1

            if currentSetting == 1:
                self.libraryName = self.GetNextLine().strip()

            if currentSetting == 2:
                self.libraryDirectory = self.GetNextLine().strip()

            if currentSetting == 3:
                self.outputDirectory = self.GetNextLine().strip()

        self.ResetReader()
