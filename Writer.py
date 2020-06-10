from PythonFileLibrary.HelperFunctions import *


"""
    Writer.py

    Writes down documentation.
"""
class Writer:
    def __init__(self, libraryName, outputFileName):
        self.libraryName = libraryName
        self.outputFileName = outputFileName + r"\\BuiltInVariables.txt"
        self.original = OpenFileSafely(r"Input\\BuiltInVariables.txt", "r", True)
        self.docs = OpenFileSafely(r"Output\\Docs.txt", "w+", True)
        self.copy = OpenFileSafely(r"Output\\BuiltInVariables_Copy.txt", "w+", True)

        # Check if any files couldn't have been opened.
        self.canWrite = not OneIs((self.original, self.docs, self.copy), None)

    # Write down the documentation of a function / variable.
    def WriteDoc(self, group, name, description):
        if self.canWrite:
            newDoc = "%s,  %s,  V2,  feat_NaturalLanguageInActive,    noFeatRest,       F, B,   %s; // %s" % (self.libraryName, group, name, description)
            self.docs.write(newDoc + '\n\n')

    # Dumps Docs.txt onto BuildVariables_Copy.txt,
    # then BuildVariables_Copy.txt onto BuildVariables.txt
    def SaveChanges(self):
        if self.canWrite:
            # Dump 1
            self.docs.close()
            rDocs = open(r"Output\\Docs.txt", "r")

            for line in self.original:
                self.copy.write(line)

            self.copy.write("\n")

            for line in rDocs:
                self.copy.write(line)

            rDocs.close()
            self.original.close()

            # Dump 2
            self.original = OpenFileSafely(self.outputFileName, "w+", False)
            self.copy = OpenFileSafely(r"Output\\BuiltInVariables_Copy.txt", "r", True)

            for line in self.copy:
                self.original.write(line)

