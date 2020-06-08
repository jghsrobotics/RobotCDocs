from Writer import *
from Searcher import *

writer = Writer()

if writer.canWrite:
    searcher = Searcher()

    for file in searcher.ListRobotCFiles(searcher.rootDirectory):
        scanner = Scanner(file)

        for info in scanner.GetDocumentation():
            print((info[0], info[1], info[2]))
            writer.WriteDoc(info[0], info[1], info[2])



    writer.SaveChanges()