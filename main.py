from Writer import *
from Scanner import *
from Searcher import *
import os

writer = Writer()

if writer.canWrite:
    searcher = Searcher()

    for file in searcher.ListRobotCFiles(searcher.rootDirectory):
        scanner = Scanner(file)

        for info in scanner.GetDocumentation():
            writer.WriteDoc(scanner.GetHeader(), info[0], info[1])



    writer.SaveChanges()