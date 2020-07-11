from SettingParser import *
from FileScanner import *
from RecursiveScanner import *
from Writer import *

settingParser = SettingParser()
recursiveScanner = RecursiveScanner(settingParser)

writer = Writer(settingParser)

for file in recursiveScanner.files:
    writer.WriteDownFile(file)
