from Writer import *
from Searcher import *

writer = Writer()

if writer.canWrite:
    searcher = Searcher()

    for file in searcher.ListRobotCFiles(searcher.rootDirectory):
        scanner = Scanner(file)

        for info in scanner.GetDocumentation():
            print((scanner.GetHeader(), info[0], info[1]))
            writer.WriteDoc(scanner.GetHeader(), info[0], info[1])



    writer.SaveChanges()