from SettingParser import *
from RecursiveScanner import *
from Writer import *

# Parse the setup.txt file to get its information.
settingParser = SettingParser()

# Recursively scan through the folder containing RobotC files (.c, .h)
# to get documentation from comments
recursiveScanner = RecursiveScanner(settingParser)

# Write down the information gathered by recursiveScanner into BuiltInVariables.txt
writer = Writer(settingParser)
for file in recursiveScanner.files:
    writer.WriteDownFile(file)
