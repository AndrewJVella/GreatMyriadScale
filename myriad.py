#This code was written without genAI because I am a big boy. I know, this is still python, not C or assembly, but while I am a big boy, I do not want to go crazy either. C would give me more control over memory, but python is certainly good enough here.

#This program is a fork of Conway's Illion Converter by kyoda
#The Great Myriad Scale is created by Andrew

import time

UNIT = ['', 'prot', 'deuter', 'trit', 'tesser',
           'pent', 'hect', 'hebdom', 'oct', 'enat']
TEN = ['', 'decat', 'icost', 'tricont', 'tetracont', 'pentacont',
       'hexacont', 'heptacont', 'octacont', 'enneacont']
BIGS = ['hecaton', 'great']

SUFFIX = "iad"

MAX = 1000

def main():

    print("This program is a proof of concept for the Great Myriad Scale.\nThis scale names large numbers with myriads, rather than millions.\nYou can find more details on that in the readme.\nThis program is a fork of \"Conway's illion Converter\" by kyoda")

    PickNumberLoop()

def displayloop():
    while True:
        list(10000, 1, 1, 150)
        print("\n" * 150)
        sleep(3)

def PickNumberLoop():
    i = "Lorem Ipsum"
    while (not i == ""):
        i = input("\nGive a power of ten (10^n), and get its name in this scale.\n> ")
        printTenPower(i)

def list(end = 1000, skip = 1, start = 1, millis = 0):

    i = start
    while i < end + skip:
        printTenPower(i)
        i += skip
        time.sleep(millis / 1000)

def printTenPower(e):
    #this was originally written for powers of the myriad
    try:
        tenners = ["one", "ten", "one hundred", "ten hundred"]
        out = tenners[int(e) % 4]
    except ValueError:
        print("Value Error")
        return

    i = int(e) // 4
    m =  myriad(i)
    if not m == "" and int(i) > 9999999:  #seven nines
        m = greatsTruncator(m)

    if (not m == ""):
        out = out + " " + m
    print("10^" + str(e) + " is called\n\"" + str(out) + "\"")

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
        n = int(n)
        if n < 0:
            n = n * -1
            suffix = suffix + "th"
    except ValueError:
        #print(' an error :(')
        return ""
    if n > 10 ** MAX:
        return ""
    #edge cases
    if n == 0:
        return '' #one
    if n == 1:
            return 'myriad'
    if n == 11:
        return 'hen' + TEN[1] + suffix
    if n == 12:
            return 'do' + TEN[1] + suffix
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
            #print(str(n) + "," + str(g) + " -> " + base(g))
            return BIGS[1] + " " + base(g)
        if g > 1 and m > 0:
            return myriad(m % 10000) + " " + BIGS[1] + " " + base(g)

if __name__ == "__main__":
    main()
