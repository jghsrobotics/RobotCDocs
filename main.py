from Writer import *
from Searcher import *
from SettingParser import *

parser = SettingParser("setup.txt")
parser.ParseFile()

writer = Writer(parser.libraryName, parser.outputDirectory)

if writer.canWrite:
    searcher = Searcher(parser.rootDirectory)

    for file in searcher.ListRobotCFiles(searcher.rootDirectory):
        scanner = Scanner(file)

        for info in scanner.GetDocumentation():
            print((info[0], info[1], info[2]))
            writer.WriteDoc(info[0], info[1], info[2])



    writer.SaveChanges()