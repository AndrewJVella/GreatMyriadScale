#This code was written without genAI because I am a big boy. I know, this is still python, not C or assembly, but while I am a big boy, I do not want to go crazy either. C would give me more control over memory, but python is certainly good enough here.


UNIT = ['', 'prot', 'deuter', 'trit', 'tetar',
           'pempt', 'hect', 'hebdom', 'ogd', 'enat']
TEN = ['', 'decat', 'icos', 'tricont', 'tetracont', 'pentacont',
       'hexacont', 'heptacont', 'octacont', 'enneacont']
BIGS = ['hecat', 'great']


def main():
    giveInput()

def giveInput():
    i = "Lorem Ipsum"
    while (not i == ""):
        i = input("give number\n> ")
        print(myriad(i))

def list(end = 10000, skip = 1, start = 1):

    i = start
    while i < end + skip:
        print(str(i) +"\t"+ myriad(i))
        i += skip

def myriad(n):

    #input sanitization
    try:
        n = int(n)
        if n < 1:
            n = n * -1
    except ValueError:
        print('"' + str(n) + '" makes an error :(')
        return ""

    #edge cases

    if n == 0:
        return 'one'
    if n == 1:
            return 'myriad'
    if n == 11:
        return 'hen' + TEN[1] + 'iad'
    if n == 12:
            return 'do' + TEN[1] + 'iad'
    #end of edge cases
    return str(base(n)) + "iad"
def base(n):
    if n < 10:
        return UNIT[n]
    if n < 100:
        t = n // 10
        m = n % 10
        if m == 0:
            return TEN[t]
        if (m < 8): #vowels matter for the 10's. You want "conta", "cato", and "coso", but not "oo" "oe" or "th" to keep demoninations readble. 10000^17 is decato-hebdomiad 10000^18 is decat-ogdiad.
            if (t < 3):
                return TEN[t] + "o" + base(m)
            else:
                return TEN[t] + "a" + base(m)
        else:
            return TEN[t] +  base(m)

    if n < 1000:
        t = n // 100
        m = n % 100
        if t == 1:
            return BIGS[0]  + base(m)
        return base(t) + "o" + BIGS[0]  + base(m)
    if n < 10000: #here there be dragons?
        t = n // 100
        return base(n // 100) + "o" + BIGS[0]  + base(n % 100)
    if n > 9999:
        g = 0
        while n > 9999:
            n = n - 10000
            g += 1
        if g == 1 and n == 0:
            return BIGS[1] + " myr"
        if g == 1 and n > 0:
            return myriad(n) + " " + BIGS[1] + " myr"
        else:
            return myriad(n % 10000) + " " + BIGS[1] + " " + base(g)

if __name__ == "__main__":
    main()
