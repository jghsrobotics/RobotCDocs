"""
    CommentFilter.py

    Filters out the data collected by a FileScanner object to
    be compatible with RobotC's documentation. It does this by
    simply removing all spaces and types of a declaration.
"""

class CommentFilter:
    def __init__(self):
        self.filter = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM*&_1234567890"
        pass

    def removeType(self, line, index = 2) -> str:
        """
            Removes the types and spaces of a declaration recusively.
        """

        if len(line) < 2:
            return line

        if index < 2:
            index = 2

        # Given a str with 'a a', where a is a char, remove the first a recursively.
        # This effectively removes all types.

        expectedSpace = line[index - 1] # There must be a space between chars
        expectedType = line[index - 2]  # The type should be seperated by a single space
        expectedName = line[index]      # The type should come before a name

        if expectedSpace == ' ' and expectedType in self.filter and expectedName in self.filter:
            line = line[:index - 2] + line[index - 1:]
            if index - 1 != 0:
                return self.removeType(line, index - 1)

        else:
            # Move on
            if index + 1 != len(line):
                return self.removeType(line, index + 1)

        return line


    def FilterDoc(self, doc):
        functionStr = doc.declaration

        # ROBOTC hates types defined in its documentation. Remove ALL OF IT!
        functionStr = self.removeType(functionStr, 2)
        while ' ' in functionStr:
            functionStr = functionStr.replace(' ', "")

        doc.declaration = functionStr







if __name__ == "__main__":
    cm = CommentFilter()
    print(cm.removeType("void type stuff main(int i);", 2))
