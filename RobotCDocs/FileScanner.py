from PythonFileLibrary.Reader import *

"""
    FileScanner.py

    Scans a file for JSDoc-like documentation.
"""
class FileScanner(Reader):
    def __init__(self, file):
        super().__init__(file)

        self.categoryName = self.fileName.split('\\')[-1].split('.')[0]
        self.docs = []

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

        content = ""
        for line in self.GetComments():

            if self.StrAtIndex(line, ' * ', 0):
                line = line.replace(' * ', "")

                content += line

                if line[-1] != ' ':
                    content += ' '

            if '*/' in line:
                function = self.GetNextLine().strip()
                if ';' in function:
                    self.docs.append([function, content])
                content = ""
