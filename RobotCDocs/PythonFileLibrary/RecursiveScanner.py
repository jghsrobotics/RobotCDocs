import os

"""
    RecursiveScanner.py

    Recursively scans a root directory for leaf nodes and lists the files.
"""
class RecursiveScanner:
    def __init__(self, directory, whitelist):
        # List of files' names.
        self.files = []

        # List of extensions of the files wanted (.c, .h, .py, ect.)
        self.whitelist = whitelist

        # Directory of the root folder.
        self.directory = directory

        self.Scan(directory)

    def GetFileExtension(self, file):
        extensions = file.split('.')
        return '.' + extensions[-1]

    def Scan(self, directory):
        for obj in os.listdir(directory):
            # If it's a folder, keep searching. If it's a weird file, skip it.
            if '.' not in obj:
                try:
                    self.Scan(os.path.join(directory, obj))
                except:
                    pass

            else:
                # If it's a file in our whitelist, make a FileScanner for it
                for item in self.whitelist:
                    if item == self.GetFileExtension(obj):
                        self.files.append(os.path.join(directory, obj))
                        break
