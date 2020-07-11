from SettingParser import *
from FileScanner import *
from Writer import *

settingParser = SettingParser()
fileScanner = FileScanner("Helpers.h")

writer = Writer(settingParser)
writer.WriteDownFile(fileScanner)
