"""
    HelperFunctions.py

    A list of pretty helpful functions.
"""

# Opens a file safely.
def OpenFileSafely(fileName, mode, raiseError):
    try:
        # Try to open the file
        return open(fileName, mode)
    except:
        # If the file couldn't have been opened
        if raiseError:
            print("Had trouble opening %s." % fileName)
            return None

        else:
            print("%s wasn't found. Trying to create %s..." % (fileName, fileName))

            createdFile = open(fileName, "w+")
            createdFile.close()

            return OpenFileSafely(fileName, mode, False)

# Checks if at least one object in an array are equal to another object.
def OneIs(objects, value):
    for obj in objects:
        if obj is value:
            return True

    return False
