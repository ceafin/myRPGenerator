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
    return genList

def OnRoll(userRequest,numRequested):
    genFile = "./Generators/" + userRequest.strip() + ".py"
    numRolls = int(numRequested)

    x = imp.load_source("generator", genFile)
    z = x.generator()

    results = []
    for _ in range(numRolls):
        results.append(z.start())
    results.sort()

    print("+=-- Rolls --=+")
    for result in results:
        print(result)
    print("+=-----------=+\n")


if __name__ == "__main__":
    tableList=GetGeneratorList()
    userRequest = input("Which table to roll?: ")
    numRequested = input("And how many do you want?: ")
    OnRoll(userRequest,numRequested)
