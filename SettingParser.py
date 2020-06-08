from Reader import *

class SettingParser(Reader):
    def __init__(self, setupFileName):
        super().__init__(setupFileName)
        self.currentSetting = 0

        self.libraryName = "LibraryNameNotSet"
        self.rootDirectory = "RootDirectoryNotSet"
        self.outputDirectory = "OutputDirectoryNotSet"

    # Parses the file. This is where the magic happens
    def ParseFile(self):
        if self.canParse:
            currentLine = self.GetCurrentLine()

            while not self.ReachedEnd():

                # '>' indicates the start of a setting
                if '>' in currentLine:
                    self.currentSetting += 1
                    currentLine = self.GetNextLine()

                if self.currentSetting == 1:
                    self.libraryName = currentLine

                if self.currentSetting == 2:
                    self.rootDirectory = currentLine

                if self.currentSetting == 3:
                    self.outputDirectory = currentLine

                # Proceed to the next line
                currentLine = self.GetNextLine()


        else:
            print ("%s could not be parsed as it doesn't exist." % self.fileName)