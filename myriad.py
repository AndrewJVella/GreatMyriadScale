#This code was written without genAI because I am a big boy. I know, this is still python, not C or assembly, but while I am a big boy, I do not want to go crazy either. C would give me more control over memory, but python is certainly good enough here.

#This program is a fork of Conway's Illion Converter by kyoda
#The Great Myriad Scale is created by Andrew

import sys

UNIT = ['', 'prot', 'deuter', 'trit', 'tesser',
           'pent', 'hect', 'hebdom', 'oct', 'enat']
TEN = ['', 'decat', 'icost', 'tricont', 'tetracont', 'pentacont',
       'hexacont', 'heptacont', 'octacont', 'enneacont']
BIGS = ['hecaton', 'great']

SUFFIX = "iad"

DISPLAY = True

MAX = 1000

def main(arg = "", display = True):
    global DISPLAY
    DISPLAY = display #don't print anything if display is false
    #command line arg
    if len(sys.argv) > 1:
        return parseInput(sys.argv[1])

    if not arg == "": #main is called from somehwere else
        return parseInput(arg)
    dprint("\nThis program is a proof of concept for the Great Myriad Scale.\nThis scale names large numbers with myriads, rather than millions.\nYou can find more details on that in the readme.\nThis program is based on \"Conway's illion Converter\" by kyoda.")
    PickNumberLoop()

def dprint(s = ""):
    global DISPLAY
    if DISPLAY:
        print(s)

def parseInput(i):
    i = i.replace(" ", "")

    args = i.split(":")

    if len(args) < 2:
        return printTenPower(i)
    if len(args) == 2:
        return list(args[0], args[1])
    if len(args) == 3:
        return list(args[0], args[1], args[2])
    if len(args) > 3:
        return list(args[0], args[1], args[2], args[3])

def PickNumberLoop():
    i = "Lorem Ipsum"
    while (not i == ""):
        i = input("\nGive a power of ten (10^n), and get its name in the Great Myriad Scale.\nUse colons to list (start:stop:skip).\n> ")
        parseInput(i)
        dprint()


def list(start = 1, end = 1, skip = 1):

    try:
        end = int(end)
        skip = int(skip)
        start = int(start)
    except ValueError:
        print ("Value Error")
        return ""

    i = start
    while i <= end:
        #dprint(i)
        printTenPower(str(i))
        dprint()
        i += skip

def printTenPower(e):
    #this was originally written for powers of the myriad
    try:
        tenners = ["One", "Ten", "One Hundred", "Ten Hundred"]
        out = tenners[int(e) % 4]
    except ValueError:
        dprint("Value Error")
        return ""

    if int(e) < 0:
        dprint("Please use non-negative integers.")
        return

    i = int(e) // 4
    m =  myriad(i)
    if not m == "" and int(i) > 9999999:  #seven nines
        m = greatsTruncator(m)

    if (not m == ""):
        out = (out + " " + m).title()

    dprint("10^" + str(e) + " = \"" + str(out) + "\"")
    return out

def greatsTruncator(m):
    #its linear, but the "greats" can just be tallied up and trucated accordingly
    #unfortunately this code is kind of fragile and does not play nicely with refactoring
    #so it has to go in its own little function
    headIndex = 0
    writingtoOut = True
    c = 0
    greats = 0
    g = BIGS[1][0]
    r = BIGS[1][1]
    o = ""
    while c < len(m) - 1:
        if m[c] == g and m[c+1] == r:
            greats += 1
            if writingtoOut:
                headIndex = c
                writingtoOut = False
        if m[c] == " " and not m[c+1] == g:
            if greats == 1:
                o += BIGS[1]
            if greats > 1:
                o +=  myriad(greats, "ic " + BIGS[1])
            greats = 0
            writingtoOut = True
        if writingtoOut:
            o += m[c]
        c = c + 1
    return o + "d"


def myriad(n, suffix = "iad"):
    #input sanitization
    try:
        n = int(n) #the myriad function can handle negative integers
        if n < 0:
            n = n * -1
            suffix = suffix + "th"
    except ValueError:
        #dprint(' an error :(')
        return ""
    if n > 10 ** MAX:
        return ""
    #edge cases
    if n == 0:
        return '' #one
    if n == 1:
            return 'myriad'

    #end of edge cases
    return str(base(n)) + suffix

def base(n):
    if n < 10:
        return UNIT[n]
    if n < 100:
        t = n // 10
        m = n % 10
        if m == 0:
            return TEN[t]
        if (m < 8): #vowels matter for the 10's. You want "conta", "cato", and "coso", but not "oo" "oe" or "th" to keep demoninations readble. 10000^17 is decato-hebdomiad 10000^18 is decat-ogdiad.
            return TEN[t] + "o" + base(m)

        else:
            return TEN[t] +  base(m)

    if n < 1000:
        t = n // 100
        m = n % 100
        if t == 1:
            return BIGS[0] + base(m)

        return base(t) + "e" + BIGS[0]  + base(m)
    if n < 10000: #here there be dragons? I forget. Norovirus is fun.
        t = n // 100
        return base(n // 100) + "e" + BIGS[0]  + base(n % 100)
    #if n < 100000000: # great myriad to great great myriad or deuteron myriad
    else:
        g = n // 10000
        m = n % 10000
        if g == 1 and m == 0:
            return BIGS[1] + " myr"
        if g == 1 and m > 0:
            return myriad(m) + " " + BIGS[1] + " myr"
        if g > 1 and m == 0:
            #if you actually try to track the stack calls by printing base(g) before return there's a lot more than I expected. It still outputs the correct number of "greats"
            #dprint(str(n) + "," + str(g) + " -> " + base(g))
            return BIGS[1] + " " + base(g)
        if g > 1 and m > 0:
            return myriad(m % 10000) + " " + BIGS[1] + " " + base(g)

if __name__ == "__main__":
    main()
