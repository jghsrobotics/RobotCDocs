from PythonFileLibrary.Reader import *

class FileScanner(Reader):
    def __init__(self, file):
        super().__init__(file)

        self.categoryName = self.fileName.split('.')[0]

        try:
            self.Parse()
        except AssertionError as error:
            print(error)

    # Returns C style long comments.
    def GetComments(self):
        inComment = False
        for line in self.CleanRead():
            if '/*' in line:
                inComment = True

            if inComment:
                yield line.strip('\n')

            if '*/' in line:
                inComment = False


    def StrAtIndex(self, str, substr, index):
        try:
            assert str.index(substr) == index
            return True
        except:
            return False

    def Parse(self):
        assert self.canParse, "FileScanner.py: Could not open %s." % (self.fileName)

        docs = []
        content = ""
        for line in self.GetComments():

            if self.StrAtIndex(line, ' * ', 0):
                line = line.replace(' * ', "")

                content += line

                if line[-1] != ' ':
                    content += ' '

            if '*/' in line:
                docs.append([self.GetNextLine(), content])
                content = ""

        for i in docs:
            print(i)
