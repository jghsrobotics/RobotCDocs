
"""
    Writer.py

    Writes down documentation.
"""
class Writer:
    def __init__(self):
        self.canWrite = True
        self.original = self.OpenFileSafely("BuiltInVariables_OG.txt", "r", True)
        self.docs = self.OpenFileSafely("Docs.txt", "w+")
        self.output = self.OpenFileSafely("BuiltInVariables.txt", "w+")

    # Opens a file safely.
    def OpenFileSafely(self, fileName, mode, raiseError = False):
        try:
            return open(fileName, mode)
        except:
            if raiseError:
                print(fileName + " wasn't found. Files will not scanned.")
                self.canWrite = False
                return None

            else:
                print(fileName + " wasn't found. Creating file...")

                createdFile = open(fileName, "w+")
                createdFile.close()

                return self.OpenFileSafely(fileName, mode, False)

    def WriteDoc(self, group, name, description):
        if self.canWrite:
            newDoc = "Diego\'s Custom Library,  %s,  V2,  feat_NaturalLanguageInActive,    noFeatRest,       F, B,   %s; // %s" % (group, name, description)
            self.docs.write(newDoc + '\n\n')

    def SaveChanges(self):
        if self.canWrite:
            self.docs.close()
            rDocs = open("Docs.txt", "r")

            for line in self.original:
                self.output.write(line)

            self.output.write("\n")

            for line in rDocs:
                self.output.write(line)

            rDocs.close()
            self.original.close()

