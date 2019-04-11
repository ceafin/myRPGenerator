#!/usr/local/opt/python/bin/python3.7

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
    print(genList)


def OnRoll():
    genFile = "./Generators/" + "Angels" + ".py"
    numRolls = 5

    x = imp.load_source("generator", genFile)
    z = x.generator()

    results = []
    for j in range(numRolls):
        results.append(z.start())
    results.sort()

    print(results)


if __name__ == "__main__":
    GetGeneratorList()
    OnRoll()