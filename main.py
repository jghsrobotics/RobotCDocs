from Writer import *
from Scanner import *
import os

writer = Writer()

if writer.canWrite:
    scanner = Scanner("Helpers.h")

    for info in scanner.GetDocumentation():
        writer.WriteDoc(scanner.GetHeader(), info[0], info[1])

    writer.SaveChanges()