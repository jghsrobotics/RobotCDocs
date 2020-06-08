from HelperFunctions import *


"""
    Writer.py

    Writes down documentation.
"""
class Writer:
    def __init__(self, libraryName):
        self.libraryName = libraryName
        self.original = OpenFileSafely(r"Source\\BuiltInVariables.txt", "r", True)
        self.docs = OpenFileSafely(r"Output\\Docs.txt", "w+", True)
        self.output = OpenFileSafely(r"Output\\BuiltInVariables.txt", "w+", True)

        # Check if any files couldn't have been opened.
        self.canWrite = not OneIs((self.original, self.docs, self.output), None)

    # Write down the documentation of a function / variable.
    def WriteDoc(self, group, name, description):
        if self.canWrite:
            newDoc = "%s,  %s,  V2,  feat_NaturalLanguageInActive,    noFeatRest,       F, B,   %s; // %s" % (self.libraryName, group, name, description)
            self.docs.write(newDoc + '\n\n')

    # Dumps Docs.txt onto BuildVariables.txt
    def SaveChanges(self):
        if self.canWrite:
            self.docs.close()
            rDocs = open(r"Output\\Docs.txt", "r")

            for line in self.original:
                self.output.write(line)

            self.output.write("\n")

            for line in rDocs:
                self.output.write(line)

            rDocs.close()
            self.original.close()

