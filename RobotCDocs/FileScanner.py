from PythonFileLibrary.Reader import *
from Doc import *

"""
    FileScanner.py

    Scans a file for JSDoc-like documentation.
"""
class FileScanner(Reader):
    def __init__(self, file):
        super().__init__(file)

        # Given a directory (E.x. \Desktop\File.h), only save the actual file name (File.h)
        self.docFileName = self.fileName.split('\\')[-1]

        # The name of the file (E.x. "File")
        self.categoryName = self.docFileName.split('.')[0]
        self.docs = []

        try:
            self.Parse()
        except AssertionError as error:
            print(error)

    # Yield lines that have C-styule long comments. The file
    # can still be read normally using self.GetNextLine()
    # or self.SkipLine(n)
    def GetComments(self):
        inComment = False
        for line in self.CleanRead():
            if '/*' in line:
                inComment = True

            if inComment:
                # Yield the entire comment (including  '/*' and '*/')
                yield line.strip('\n')

            if '*/' in line:
                inComment = False

    # Return whether or not a subtring starts at a specific index.
    def StrAtIndex(self, str, substr, index):
        try:
            assert str.index(substr) == index
            return True
        except:
            return False

    # Parse a file. Throws an AssertionError if the file cannot be read.
    def Parse(self):
        assert self.canParse, "FileScanner.py: Could not open %s." % (self.fileName)

        doc = Doc()
        doc.category = self.categoryName
        for line in self.GetComments():

            if self.StrAtIndex(line, ' *', 0):
                line = line.replace(' * ', "")
                line = line.replace(' *', "")

                if '@' in line:

                    # Split the line into words, then get the name of the category.
                    words = line.split(' ')
                    for word in words:
                        if '@' in word:
                            doc.category = word.split('@')[-1].capitalize()
                            break

                # Join sentences together to make one long string.
                doc.description += line

                # If a sentence doesn't have a space at the end,
                # add it to preserve grammar.
                if len(line) > 0:
                    if line[-1] != ' ':
                        doc.description += ' '

            elif '/*' not in line and '*/' not in line:
                print('FileScanner.py: Warning: Line %s of %s is missing a \' *\'; Line will be skipped.' % (self.currentLine + 1, self.docFileName))



            if '*/' in line:
                # Check that the comment was right before a function or variable declaration.
                doc.declaration = self.GetNextLine().strip()
                if ';' in doc.declaration:
                    self.docs.append(doc)
                else:
                    print('FileScanner.py: Warning: Line %s of %s was skipped due to missing a declaration.' % (self.currentLine + 1, self.docFileName))

                doc = Doc()
                doc.category = self.categoryName
