"""
    Scanner.py

    Scans RobotC Files for comments.
"""

class Scanner:
    def __init__(self, fileName):
        self.canScan = True
        self.file = self.OpenFileSafely(fileName, "r")
        self.lines = []
        self.types = [
            "tMotor ",
            "tSensors ",
            "int ",
            "float ",
            "double ",
            "PIDInfo ",
            "short ",
            "bool ",
            ";",
            "task ",
            "ubyte ",
            "byte ",
            "void "
        ]

        if self.canScan:
            self.lines = self.file.readlines()

    # Opens a file safely.
    def OpenFileSafely(self, fileName, mode):
        try:
            return open(fileName, mode)
        except:
            print(fileName + " wasn't found for scanning. File will not scanned.")
            self.canScan = False
            return None

    def GetHeader(self):
        if self.canScan:
            scanning = False
            for line in self.lines:
                line = line.strip()

                # Start scan if a comment appears
                if '/*' in line:
                    scanning = True

                if scanning:
                    # Get group name; Name of file.
                    if '.h' in line:
                        return self.HeaderName(line)
        else:
            return ""

    # Get documentation info
    def GetDocumentation(self):
        if self.canScan:
            scanning = False
            insideComment = False
            desc = ""

            header = self.GetHeader()

            for line in self.lines:
                line = line.strip()

                # Start scan if a comment appears
                if '/*' in line:
                    scanning = True
                    insideComment = True

                if scanning:
                    # Skip header
                    if '.h' in line:
                        scanning = False
                        continue

                    if '[SETUP]' in line:
                        header = 'Setup'

                    # Else, try to report data and reset
                    elif self.HasType(line) and not insideComment:
                        yield (header, self.StripFunction(line), desc)
                        header = self.GetHeader()
                        desc = ""
                        scanning = False

                    # Otherwise, add to description instead
                    elif len(line) > 3:
                        desc += self.StripDescription(line)

                if '*/' in line:
                    insideComment = False
        else:
            yield []

    # Strips a function of its types.
    def StripFunction(self, func):
        stripedFunc = func

        for type in self.types:
            stripedFunc = stripedFunc.replace(type,"")

        return stripedFunc

    # Gets the name of a header
    def HeaderName(self, header):
        # Strip * of header
        header = header.replace("*", "")

        # Strip spaces of header
        header = header.replace(" ", "")

        # Strip .h of header
        header = header.replace(".h", "")

        return header

    # Get the description part of a comment
    def StripDescription(self, desc):
        return desc.replace("* ", "") + " "

    def HasType(self, str):
        for type in self.types:
            if type in str:
                return True
        return False
