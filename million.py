#runnable illion converter, fork of kyoda's illion converter

DESCRIPTION = "show name of N'th zillion number"
ISOLATE = ['ni', 'mi', 'bi', 'tri', 'quadri',
           'quinti', 'sexti', 'septi', 'octi', 'noni']
CW_UNI = ['', 'un', 'duo', 'tre', 'quattuor', 'quin', 'se',
          'septe', 'octo', 'nove']  # quinqua is changed to quin
TEN = ['', 'deci', 'viginti', 'triginta', 'quadraginta', 'quinquaginta',
       'sexaginta', 'septuaginta', 'octoginta', 'nonaginta']
HUN = ['', 'centi', 'ducenti', 'trecenti', 'quadringenti',
       'quingenti', 'sescenti', 'septingenti', 'octingenti', 'nongenti']
SIMP_UNI = ['', 'un', 'duo', 'tre', 'quattuor',
            'quin', 'sex', 'septen', 'octo', 'novem']
PREC_TEN = ['', 'N', 'MS', 'NS', 'NS', 'NS', 'N', 'N', 'MX', '']
PREC_HUN = ['', 'NX', 'N', 'NS', 'NS', 'NS', 'N', 'N', 'MX', '']

SHORT = True


def main():
    print("\nThis program is an implementation for the Conway Weschler System of Scales.\nThis system uses Latin numeric prefixes to extend the \"-illion\" numbers (\"million\", \"billion\", \"trillion\" and so on).\nThis program is based on \"Conway's illion Converter\" by kyoda.")
    PickNumberLoop()

def parseInput(i):
    global SHORT
    i = input(i)

    print()
    i = i.replace(" ", "")
    if i == ":":
        SHORT = not SHORT
        if SHORT:
            print("Short scale in use.")
        else:
            print("Long scale in use.")
        return

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
    global SHORT
    i = "Lorem Ipsum"
    s = "Short"
    while (not i == ""):
        if SHORT:
            s = "Short"
        if not SHORT:
            s = "Long"
        i = parseInput("\nGive a power of ten (10^n), and get its name in the Conway-Weschler " + s +  " Scale.\nUse colons to list (start:stop:skip).\nType a single colon to switch between the short and long scales.\n> ")

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
        #print(i)
        printTenPower(str(i))
        print()
        i += skip

def printTenPower(e, short = None):
    global SHORT

    if not short == None:
        SHORT = short

    try:
        e = int(e)
    except ValueError:
        print("Value Error")
        return ""
    #long scale by default
    scaleFactor = 6
    tenners = ["One", "Ten", "One Hundred, One Thousand, Ten Thousand, One Hundred Thousand"]

    #behold the short scale
    if SHORT:

        tenners = ["One", "Ten", "One Hundred"]
        scaleFactor = 3
        if e == 0:
            print("10^0 = \"One\"")
            return "One"
        if e == 1:
            print("10^1 = \"Ten\"")
            return "Ten"
        if e == 2:
            print("10^2 = \"One Hundred\"")
            return "One Hundred"
        if e == 3:
            print("10^3 = \"One Thousand\"")
            return "One Thousand"
        if e == 4:
            print("10^4 = \"Ten Thousand\"")
            return "Ten Thousand"
        if e == 5:
            print("10^5 = \"One Hundred Thousand\"")
            return "One Hundred Thousand"
        else:
            e = e - 3

    out = tenners[e % scaleFactor]

    if e < 0:
        print("Please use non-negative integers.")
        return

    i = e // scaleFactor
    m =  llion(i)

    if (not m == ""):
        out = (out + " " + m).title()
    if SHORT:
        e = e + 3
    print("10^" + str(e) + " = \"" + str(out) + "\"")
    return out

def llion(n, modified = False):
    if n < 1:
        return ''
    name = ''
    while n > 999:
        name = concat(n % 1000, name, modified)
        n = n // 1000
    name = concat(n, name, modified)
    return name


def concat(n, suffix, modified):
    result = base(n, modified) + suffix
    if suffix == '':
        result += 'on'
    return result


def base(n, modified):
    if n < 10:
        return ISOLATE[n] + 'lli'
    unit = n % 10
    ten = (n//10) % 10
    hun = n//100
    if ten == 0:
        prec = PREC_HUN[hun]
    else:
        prec = PREC_TEN[ten]
    if modified:
        name = SIMP_UNI[unit]
    else:
        name = CW_UNI[unit]
        if unit == 3 or unit == 6:
            if 'S' in prec:
                name += 's'
            if 'X' in prec:
                if unit == 3:
                    name = 'tres'
                else:
                    name = 'sex'
        if unit == 7 or unit == 9:
            if 'M' in prec:
                name += 'm'
            if 'N' in prec:
                name += 'n'
    name += TEN[ten]
    name += HUN[hun]
    return name[:-1] + 'illi'  # Replace the final vowel



if __name__ == "__main__":
    main()
