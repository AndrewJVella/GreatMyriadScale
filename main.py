#from scales import myriad
#from scales import million
import tables
import sys

def main():
    tables.main()


def main(arg = "", display = True):
    #command line arg
    if len(sys.argv) > 1:
        return parseInput(sys.argv[1])
    #main is called from somehwere else
    if not arg == "":
        return parseInput(arg)

    print("\nThis program is a proof of concept for the Great Myriad Scale.\nThis scale names large numbers with myriads, rather than millions.\nYou can find more details on that in the readme.\nThis program is based on \"Conway's illion Converter\" by kyoda.")
    PickNumberLoop()


def parseInput(i):
    i = i.replace(" ", "")

    args = i.split(":")

    if len(args) < 2:
        return doThings([i])
    if len(args) == 2:
        return list(args[0], args[1])
    if len(args) > 3:
        return list(args[0], args[1], args[2])


def PickNumberLoop():
    i = "Lorem Ipsum"
    while (not i == ""):
        i = input("\nGive a power of ten (10^n), and get its name in the Great Myriad Scale.\nUse colons to list (start:stop:skip).\n> ")
        parseInput(i)
        print()


def list(start = 1, end = 1, skip = 1):

    try:
        end = int(end)
        skip = int(skip)
        start = int(start)
    except ValueError:
        print ("Value Error")
        return ""

    doThings(range(start, end, skip))

def doThings(i):
    print(tables.getCustomTable(i))
    return


main()
