from SettingParser import *
from FileScanner import *
from Writer import *

settingParser = SettingParser()
fileScanner = FileScanner("Helpers.h")

writer = Writer(settingParser)
writer.WriteDownFile(fileScanner)

#Diego's Custom Library,  Controllers,  V2,  feat_NaturalLanguageInActive,    noFeatRest,       F, B,   RightArcadeControl(); // Arcade control with the right joystick. Supports slewing motors.
