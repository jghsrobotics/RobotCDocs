from PythonFileLibrary.HelperFunctions import *


class Writer:
    def __init__(self, settingParser):
        self.libraryName = settingParser.libraryName
        self.outputDirectory = settingParser.outputDirectory
        self.template = "%s,  %s,  V2,  feat_NaturalLanguageInActive,    noFeatRest,       F, B,   %s // %s"

        self.inputFile = OpenFileSafely('Input/BuiltInVariables.txt', 'r', True)
        self.canParse = self.inputFile is not None
        self.outputFile = open(self.outputDirectory + 'BuiltInVariables.txt', 'w+')

        try:
            self.CopyInput()
        except AssertionError as error:
            print(error)

    def CopyInput(self):
        assert self.canParse, "Writer.py: Could not read from BuiltInVariables.txt."
        self.outputFile.writelines(self.inputFile.readlines())
        self.outputFile.write("\n")

    def WriteDownFile(self, fileScanner):
        for doc in fileScanner.docs:

            functionDoc = self.template % (self.libraryName, fileScanner.categoryName, doc[0], doc[1])

            self.outputFile.write(functionDoc + "\n")
            self.outputFile.write("\n")
