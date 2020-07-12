"""
    CommentFilter.py

    Filters out the data collected by a FileScanner object to
    be compatible with RobotC's documentation.
"""

class CommentFilter:
    def __init__(self):
        self.types = [
            "short",
            "unsigned",
            "long",
            "int",
            "float",
            "double",
            "task",
            "byte",
            "void",
            "ubyte",
            "tMotor",
            "tSensors",
            "bool",
            "PIDInfo"
        ]

    def FilterDoc(self, doc):
        functionStr = doc.declaration

        # ROBOTC hates types defined in its documentation. Remove ALL OF IT!
        for type in self.types:
            functionStr = functionStr.replace(type + '* ', "")
            functionStr = functionStr.replace(type + ' ', "")

        doc.declaration = functionStr
