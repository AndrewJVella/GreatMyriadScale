from tabulate import tabulate
import myriad
import million


def main():
    print(getMyriadTable())
    print(getScaleTable())
    #input("Push enter to close")

def genericTable():
    # Column headers
    headers = ["Name", "Age", "Profession"]
    # Data for the table
    data =  [["Alice", "24", "Engineer"],
            ["Bob", "27", "Designer"],
            ["Charlie", "22", "Artist"]]


    # Generate Markdown table
    markdown_table = tabulate(data, headers, tablefmt="pipe", stralign="center")
    print(markdown_table)


def getMyriadTable():
    headers = ["e", "Name", "e", "Name", "e", "Name"]
    data = [["4", "<m>", "48", "<m>", "120", "<m>"],
            ["8", "<m>", "52", "<m>", "160", "<m>"],
            ["12", "<m>", "56", "<m>", "200", "<m>"],
            ["16", "<m>", "60", "<m>", "240", "<m>"],
            ["20", "<m>", "64", "<m>", "280", "<m>"],
            ["24", "<m>", "68", "<m>", "320", "<m>"],
            ["28", "<m>", "72", "<m>", "360", "<m>"],
            ["32", "<m>", "76", "<m>", "400", "<m>"],
            ["36", "<m>", "80", "<m>", "2000", "<m>"],
            ["40", "<m>", "84", "<m>", "4000", "<m>"],
            ["44", "<m>", "88", "<m>", "40000", "<m>"]]

    return tablegen(headers, data, "The Myriads")

def getScaleTable():
    headers = ["e", "Great Myriad", "Conway-Weschler Short", "Conway-Weschler Long"]
    data = [["0", "<m>", "<s>", "<l>"]]
    t = 1
    while (t < 1000000):
        for i in range (1 * t, 8 * t, 1 * t):
            data.append([str(i), "<m>", "<s>", "<l>"])
        for i in range (8 * t, 100 * t, 4 * t):
            data.append([str(i), "<m>", "<s>", "<l>"])
        t = t * 100
    data.append([str(t), "<m>", "<s>", "<l>"])

    return tablegen(headers, data, "Table of Scales")



def tablegen(headers, data, title = ""):
        #data is a 2d array and headers is a 1d array

        # I want this to be able to parse a tag and replace it with something
        # A tag looks like <this>

        i = 0
        j = 0
        while i < len(data): #for i in data does not work
            j = 0
            while j < len(data[i]):
                if data[i][j][0] == "<": #j is a tag
                    #print(data[i][j])
                    if headers[j - 1] == "e":
                        data[i][j] = tagparse(data[i][j] + data[i][j - 1]) #table 1 is actually an edge case
                    else:
                        data[i][j] = tagparse(data[i][j] + data[i][0])

                    #print(data[i][j])
                j += 1
                #print(i, j)
            i += 1

        # Generate Markdown table
        markdown_table = tabulate(data, headers, tablefmt="pipe", stralign="left")
        return "\n"+ title + "\n\n" +  markdown_table

def tagparse(tag):
    type = tag[1]
    n = tag.strip("<" + tag[1] + ">")

    #print("n = " + str(n))

    if type == "m":
        return myriad.main(n, False) #n, prints off
    if type == "s":
        return million.main(n, True, False) #n, short scale, prints off
    if type == "l":
        return million.main(n, False, False)  #n, long scale, prints off
    return -1

main()
