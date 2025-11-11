
import myriad
import million
import tables
import sys
import os

def main():
    tables.main()


def main(arg = "", display = True):
    #command line arg
    if len(sys.argv) > 1:
        return parseInput(sys.argv[1])
    #main is called from somehwere else
    if not arg == "":
        return parseInput(arg)
    PickNumberLoop()


def parseInput(i):

    if (i == ""):
        return ""

    i = i.replace(" ", "")[0] #get a number

    if (i == "1"):
        myriad.main()
        return
    if (i == "2"):
        million.main()
        return
    if (i == "3"):
        tables.main()
        return
    else:
        print("Silly bean, pick a number!\n")
    return




def PickNumberLoop():
    i = "Lorem Ipsum"
    tables.main()
    while (not i == ""):
        i = input("Select an option:\n1. Generate Myriads\n2. Generate Millions\n3. Tables (Quick Help)\n> ")
        parseInput(i)
        print()




main()
