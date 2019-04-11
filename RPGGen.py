#!/usr/local/bin/python3

import os
import glob
import imp


def GetGeneratorList():
    # Get list of generators
    genList = []
    path = "./Generators/"
    for infile in glob.glob(os.path.join(path, "*.py")):
        infile = os.path.splitext(os.path.basename(infile))[0]
        if not infile.startswith("_"):
            genList.append(infile)

    print("+=-- List --=+")
    for gen in genList:
        print(gen)
    print("+=-----------=+\n")


def OnRoll():
    genFile = "./Generators/" + "Book Titles" + ".py"
    numRolls = 5

    x = imp.load_source("generator", genFile)
    z = x.generator()

    results = []
    for j in range(numRolls):
        results.append(z.start())
    results.sort()

    print("+=-- Rolls --=+")
    for result in results:
        print(result)
    print("+=-----------=+\n")


if __name__ == "__main__":
    GetGeneratorList()
    OnRoll()
