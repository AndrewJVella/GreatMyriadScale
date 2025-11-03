# The Great Myriad Scale

The Great Myriad Scale is intended to be a practical convention for describing impractically large numbers. To introduce this passion project, it is simpler to start with what it is not. This is not a notation, like scientific or engineering notation. Nor is this a sales pitch to replace the scale you already count in. This is also not just an arbitrary list of made up big numbers. This scale is designed to be tested, and implemented, so that if you encounter some absurdly large number with a name long and strange, you can think in myriads, and scale it to size. A passion project about ancient Greek counting may seem odd, but if you would like to try an implementation of this scale, there is a python3 program on the Github repository for this page, linked in sources.

## Design of the Scale

So you might be wondering what makes this project a scale, rather than a list of arbitrary numbers and made up names? The Great Myriad Scale was written with design criteria in mind, to achieve a primary goal: this scale should actually be countable. Someone should be able to start from one and (given enough time) count all of the natural numbers, one by one, two, three, all the way to the largest denominations, and on to infinity; every number in between one and a great myriad should have a useful name, constructed from a set of denominations:

* Denominations are numbers whose names can be used to construct the names of other numbers, including one, ten, one hundred, one thousand, one myriad, and larger derivatives...

* The value of a denomination is constant. "One Hundred" always refers to 100, the square of ten. Name conflicts are not allowed. Names must be distinct, and pronounceable. So arbitrary names like "abcd" or "wxyz" are not allowed.   

* The names of non-denominational numbers are constructed from denominations, with the largest in the middle, products on the left, and sums on the right, such that (2 * 100 + 3) is "two hundred three".

* Denominations are always named according to one consistent scheme, which is constant throughout the entire scale. This scheme is not arbitrary, but based on a denomination, and compared to it with minimal edge cases. This includes naming powers of the myriad with latinized Ancient Greek, or powers of the million with Latin. In these examples, larger denominations share an etymology with the denomination on which they are based.

* A denomination can be no larger than the square of a preceding, smaller denomination (with exception for denominations which are there own squares). In other words "one myriad, myriad" may technically describe a number, but "one myriad, myriad, myriad" is just verbose, so is best to name that something shorter. Of course, there are only so many arrangements of letters, so a largest denomination must eventually be reached, but all smaller denominations that can follow this rule, will follow this rule.


## Defining the Myriad

First off, what is a myriad? So, one hundred is the square of ten, and one myriad is the square of one hundred. In other words, a myriad is equal to ten to the power of four (1,0000). Commas group four digits in this scale, so the square of a myriad is written as (1,0000,0000) What is the square of a myriad called? We will get to that. Let's start with a table to count from one to one myriad:

| n  | Name   | n  | Name       | n      | Name                       |      
|----|--------|----|------------|--------|----------------------------|
| 1  | One    | 12 | Twelve     | 30     | Thirty                     |
| 2  | Two    | 13 | Thirteen   | 40     | Forty                      |
| 3  | Three  | 14 | Fourteen   | 50     | Fifty                      |
| 4  | Four   | 15 | Fifteen    | 60     | Sixty                      |
| 5  | Five   | 16 | Sixteen    | 70     | Seventy                    |
| 6  | Six    | 17 | Seventeen  | 80     | Eighty                     |
| 7  | Seven  | 18 | Eighteen   | 90     | Ninety                     |
| 8  | Eight  | 19 | Nineteen   | 100    | One Hundred                |
| 9  | Nine   | 20 | Twenty     | 500    | Five Hundred               |
| 10 | Ten    | 21 | Twenty One | 1000   | Ten Hundred (One Thousand) |
| 11 | Eleven | 22 | Twenty Two | 1,0000 | One Myriad  (Ten Thousand) |

Now it's time to get to that square of a myriad, and the larger powers.

## The Myriad Powers

In this scale each power of the myriad get an ancient Greek prefix and an "-iad" suffix. For example "deuteriad" is a myriad to the second power. it is named by shortening "deuteros myriad", with "deuteros" referring to "second". Each successive power follows this scheme:   

| n  | Name        | n  | Name            | n      | Name             |    
|----|---------------|----|-----------------|--------|------------------|
| 1  | Myriad        | 12 | Decatodeuteriad | 30     | Tricontiad       |
| 2  | Deuteriad     | 13 | Decatotritiad   | 40     | Tetracontiad     |
| 3  | Tritiad       | 14 | Decatotesseriad | 50     | Pentacontiad     |
| 4  | Tesseriad     | 15 | Decatopentiad   | 60     | Hexacontiad      |
| 5  | Pentiad       | 16 | Decatohectiad   | 70     | Heptacontiad     |
| 6  | Hectiad       | 17 | Decatohebdomiad | 80     | Octacontiad      |
| 7  | Hebdomiad     | 18 | Decatoctiad     | 90     | Enneacontiad     |
| 8  | Octiad        | 19 | Decatenatiad    | 100    | Hecatoniad       |
| 9  | Enatiad       | 20 | Icostiad        | 500    | Pentehecatoniad  |
| 10 | Decatiad      | 21 | Icostoprotiad   | 1000   | Decatohecatoniad |
| 11 | Decatoprotiad | 22 | Icostodeuteriad | 1,0000 | Great Myriad     |

Each power of the myriad is named in this pattern until the Great Myriad, which gives this scale its name. The Great Myriad is equal to the myriad raised to the power of a myriad, which is ten to the power of forty thousand. The powers of the Great Myriad are also named with "Great", such that the square of the Great Myriad is the "Great Deuteriad", the cube of the Great Myriad is the "Great Tritiad", and so on. Is that it? No, of course there is more to discuss. Infinity is very big.

## The Great Myriads

Of course, by raising the Great Myriad to the power of a myriad, we get a "Great, Great Myriad". Raise this to the power of a myriad again to get  a "Great, Great, Great Myriad" and so on. To keep names short, a adjectival naming scheme is used (swapping the  suffix used in the above table for "-ic"). The "Great, Great Myriad" is called the "Deuteric Great Myriad". The "Great, Great, Great Myriad" is called the "Tritic Great Myriad", and so on according to the following table, with each item Each item in row n equal to 1,0000^(1,0000^n)

| n  | Name         | n  | Name           | n      | Name                   |    
|:--:|:------------:|:--:|:--------------:|:------:|:----------------------:|
| 1  | Great        | 12 | Decatodueteric | 30     | Tricontic              |
| 2  | Deuteric     | 13 | Decatotritic   | 40     | Tetracontic            |
| 3  | Tritic       | 14 | Decatotesseric | 50     | Pentacontic            |
| 4  | Tesseric     | 15 | Decatopentic   | 60     | Hexacontic             |
| 5  | Pentic       | 16 | Decatohectic   | 70     | Heptacontic            |
| 6  | Hectic       | 17 | Decatohebdomic | 80     | Octacontic             |
| 7  | Hebdomic     | 18 | Decatoctic     | 90     | Enneacontic            |
| 8  | Octic        | 19 | Decatoenatic   | 100    | Hecatonic              |
| 9  | Enatic       | 20 | Icostic        | 500    | Pentehecatonic         |
| 10 | Decatic      | 21 | Icostoprotic   | 1000   | Decatehecatonic        |
| 11 | Decatoprotic | 22 | Icostodeuteric | 1,0000 | Myriadic               |

This table grows so fast, that it becomes difficult to describe numbers this large, even in powers of a myriad. For example, a myriad to the power of a tritiad (1,0000^1,0000,0000,0000) is a tritic great myriad, but a myriad to the power of a tritiad-eleven-hundred-eleven-deuteriad-eleven-hundred-eleven-myriad-eleven-hundred-eleven (1,0000^1,1111,1111,1111) is a "decatoprotohecatondecatoprotiad great decatoprotohecatondecatoprotiad great decatoprotohecatondecatoprotiad great myriad". This all gets very repetitive, so its best to truncate insignificant figures.

"But wait!" you shout, "If a myriad to a myriad is a great myriad, and a myriad to a great myriad is a myriadic great myriad, then, surely, a myriadic great myriad is followed by a great myriadic great myriad in an extension of the above table!" You catch your breath. "A myriad to a myriadic great myriad needs a name, and then a myriad to that needs a name and so on!" Ok, a myriad to a myriadic great myriad is a "myriadeuterogonic great myriad", and a myriad to a myriadeuterogonic great myriad is a "myriatritogonic great myriad", and so on. The "-gon" suffix is applied in the same manner that the "-ic" and "-iad" suffixes are applied in respective tables.


## Constructing Cardinals, Ordinals, and Fractions

Counting the cardinal numbers between large myriads is done as it would be for any conventional denomination: largest in the middle, multipliers on the left, sums on the right. For example, one hundred times two, plus two is "two hundred, two" or "two hundred and two". Therefore, A great myriad times a myriad is a "myriad great myriad". Add one hundred to this and you get "one myriad great myriad, one hundred".

Ordinals are used for listing items; such as first, second, and third. The ordinals below the myriad are conventional: cardinal "ten" is paired with ordinal "tenth", hundred is paired with hundredth, thousand is paired with thousandth. Thus, cardinal "myriad" is paired with "myriadth", "deuteriad" with "deuteriadth", and "great myriad" with "great myriadth". Each cardinal has an ordinal, and these ordinals can be used to denote fractions (in the same manner that ordinals are conventionally used). One over a great myriad is "one great myriadth". Double that for "two great myraidths", and so on.  

## Scale Variations

Say, for the sake of argument, that you really like the short scale, but not the Latin. You want to count with powers of one thousand, rather than powers of one myriad, or of one million. Well, you can use "chilliads" to count in the "Great Chilliad" Scale. "Chilliad" refers to one thousand, and the square of one thousand would be a "deuterilliad", from "deuteros-chilliad". You can then substitute the third power for "tritilliad", from "Tritos-Chilliad" and continue on accordingly.

If you instead want a super long scale, you can be like mathematician Donald Knuth, and set each new denomination to the square of the previous one. One hundred is the square of ten, and one myriad is the square of one hundred. Then, in Knuth's "Supernatural Numbers", "one myllion" is the square of one myriad, and the square of that is a "byllion". It's easy to rename the "myllion" to a "deuteroniad", and the "byllion" to a "tritoniad", and then continue onward to construct a "Great Myrioniad Scale".

## Why?

Well, there are only so many names, there can only be so much wordplay. To keep all the numbers countable, their names needed to be constructed from smaller numbers. Sure, you can start naming with hyperoperations, but they grow faster, and faster and soon you have an unstable scaffold stretched over growing, turbulent voids ever more difficult to bridge. If you cannot count to a number, then such a number is really a vague suggestion of magnitude, a dream of many zeroes... Oh, you meant "Why invent this counting scale thing anyway? Millions are fine, and we already have scientific notation, and who would ever count from one to 'myriamyriagonic great myriad' anyway?" Well, have you ever played one of those incremental video games, with all the numbers going up to astronomical absurdity? You wake up to "Hey, while you were sleeping, you got twenty quattuorvigintillion points in the tower of tumbleweeds!", and you remember all the sheep you counted last night, hoping for rest, because in the morning, you have a fracture to tend. You have to prevent muscular atrophy by isometrically flexing a muscle several hundred times, and that means even more counting. So you make up new names for new numbers, to spice it up.

You ask yourself "Where do all the number names come from anyway, and when do we run out?" and lo, the rabbit hole! It opens before you to a wonderland of Latin and "googology", and before you realize it you have let the number goblins in. They shout "We want an incremental game! One where players can read all the numbers!" They jump on the bed. "Notations! Bah! Fie on notations!" The number goblins demand a sense of scale. "Notations transform orders of magnitude into mere increments! Madness! People need names! Names!" They grab hold of the bed knobs and shake. The leader shouts in your ear "Don't you understand?! Do it for Archimedes!" The chanting begins. "Conway! Weschler! Knuth!". You are surrounded in a cacophonous, cantankerous, chorus of contention! Then, in unison, a deep breath, and the call of a great horn. "Millinillinillinillinyllion!" With this incantation you are changed, goblinified! There is only one way to lift the spell! Give them their tables, and their powers of ten, so that they might count in numerological novelty until the end of all things!


## Footnotes and (Additional) Trivia
* In the Great Myriad Scale "hecto" refers to 6, as in the ordinal "hektos", but "hecto" can also refer to one hundred, as in "hectogon". To prevent confusion, "Hecaton" is used in place of "hecto", where it would refer to one hundred. Thus "hectiad" is a myriad to the sixth and "hecatoniad" is a myriad to the one hundredth. "Hendecatos" and "Dodecatos" (for 11 and 12) produce similar edge cases, and so, are unused.  Greco-English linguistics is difficult. Nomenclature for this scale is (inexpertly) chosen for readability to a contemporary English speaker. 
* An apeirogon has an infinite number of sides; "apeiro" gives the Great Myriad Scale the "Apeiriad" and the "Apeiron Myriad"
* Archimedes' largest Sand Number (the largest described in The Sand Reckoner) is equal to 10^(8 * 10^16), or a "Tesseron Deuteriad".
* "Cola's Enumeration" and the "Ordinal Myriad Scale" are previous attempts to enumerate large numbers, using the Conway Wechsler system, Greek ordinals, and hyperoperations. Ultimately, it is important that each name for a large number is based on the names of smaller numbers, rather than operations or notations. The numbers between "novel numbers", or "milestone numbers", also need to be nameable.


## Sources
* [Github Repository for this Page](https://github.com/AndrewJVella/GreatMyriadScale/tree/main)
* [Ancient Greek Numbers](https://en.wiktionary.org/wiki/%CF%84%CE%AD%CF%83%CF%83%CE%B1%CF%81%CE%B5%CF%82)
* [Archimedes' Sand Number](https://en.wikipedia.org/wiki/The_Sand_Reckoner)
* [Conway's illion Converter](https://kyodaisuu.github.io/illion/conway.html)
* [Conway-Weschler System](https://kyodaisuu.github.io/illion/index.html)
* [Hyperoperation](https://en.wikipedia.org/wiki/Hyperoperation)
* [List of Polygons and Greek Ordinals](https://en.wikipedia.org/wiki/List_of_polygons)
* [Myriad](https://en.wikipedia.org/wiki/Myriad)
* [Knuth's Supernatural Numbers](https://mrob.com/pub/math/largenum-2.html#yllion)


## Tables

Great Myriad Scale vs Conway-Weschler Short Scale

| e       | Great Myriad                          | Conway-Weschler Short                               |      
|:-------:|:-------------------------------------:|:---------------------------------------------------:|
| 0       | One                                   | One                                                 |
| 1       | Ten                                   | Ten                                                 |
| 2       | One Hundred                           | One Hundred                                         |
| 3       | Ten Hundred                           | One Thousand                                        |
| 4       | One Myriad                            | Ten Thousand                                        |
| 5       | Ten Myriad                            | One Hundred Thousand                                |
| 6       | One Hundred Myriad                    | One Million                                         |
| 7       | Ten Hundred Myriad                    | Ten Million                                         |
| 8       | One Deuteriad                         | One Hundred Million                                 |
| 12      | One Tritiad                           | One Trillion                                        |
| 16      | One Tesseriad                         | Ten Quadrillion                                     |
| 20      | One Pentiad                           | One Hundred Quintillion                             |   
| 24      | One Hectiad                           | One Septillion                                      |
| 28      | One Hebdomiad                         | Ten Octillion                                       |
| 32      | One Octiad                            | One Hundred Nonillion                               |
| 36      | One Enatiad                           | One Undecillion                                     |
| 40      | One Decatiad                          | Ten Duodecillion                                    |
| 44      | One Decatoprotiad                     | One Hundred Tredecillion                            |
| 48      | One Decatodeuteriad                   | One Quindecillion                                   |
| 52      | One Decatotritiad                     | Ten Sexdecillion                                    |
| 56      | One Decatotesseriad                   | One Hundred Septendecillion                         |
| 60      | One Decatopentiad                     | One Novendecillion                                  |
| 64      | One Decatohectiad                     | Ten Vigintillion                                    |
| 68      | One Decatohebdomiad                   | One Hundred Unvigintillion                          |
| 72      | One Decatoctiad                       | One Tresvigintillion                                |
| 76      | One Decatoenatiad                     | Ten Quattuorvigintillion                            |
| 80      | One Icosiad                           | One Hundred Quinvigintillion                        |
| 84      | One Icostoprotiad                     | One Septenvigintillion                              |
| 88      | One Icostodeuteriad                   | Ten Octovigintillion                                |
| 92      | One Icostotritiad                     | One Hundred Novenvigintillion                       |
| 96      | One Icostotesseriad                   | One Untrigintillion                                 |
| 100     | One Icostopentiad                     | Ten Duotrigintillion                                |
| 200     | One Pentacontiad                      | One Hundred Quinsexagintillion                      |
| 400     | One Hecatoniad                        | Ten Duotrigintacentillion                           |
| 800     | One Deuterohecatoniad                 | One Hundred Quinsexagintaducentillion               |
| 1000    | One Deuterohecatonpentacontiad        | Ten Duotrigintatrecentillion                        |
| 2000    | One Pentahecatoniad                   | One Hundred Quinsexagintasescentillion              |
| 4000    | One Decatohecatoniad                  | Ten Milliduotrigintatrecentillion                   |
| 8000    | One Icostehecatoniad                  | One Hundred Billiquinsexagintasescentillion         |
| 10000   | One Icostopentehecatoniad             | Ten Trilliduotrigintatrecentillion                  |
| 20000   | One Pentacontahecatoniad              | One Hundred Sextilliquinsexagintasescentillion      |
| 40000   | One Great Myriad                      | Ten Tredecilliduotrigintatrecentillion              |
| 80000   | One Great Deuteriad                   | One Hundred Sesvigintilliquinsexagintasescentillion |

Nomenclature Table

| n  | Name         | n  | Name            | n      | Name                     |    
|----|--------------|----|-----------------|--------|--------------------------|
| 1  | Protos       | 12 | Decatodeuteros  | 30     | Tricontad                |
| 2  | Deuteros     | 13 | Decatotritos    | 40     | Tetracontad              |
| 3  | Tritos       | 14 | Decatotesseros  | 50     | Pentacontad              |
| 4  | Tesseres     | 15 | Decatopentos    | 60     | Hexacontad               |
| 5  | Pentad       | 16 | Decatohectos    | 70     | Heptacontad              |
| 6  | Hectos       | 17 | Decatohebdomos  | 80     | Octacontad               |
| 7  | Hebdomos     | 18 | Decatogdos      | 90     | Enneacontad              |
| 8  | Octad        | 19 | Decatenatos     | 100    | Hecaton                  |
| 9  | Enatos       | 20 | Icostos         | 500    | Pentehecaton             |
| 10 | Decatos      | 21 | Icostoprotos    | 1000   | Decatohecaton (Chilliad) |
| 11 | Decatoprotos | 22 | Icostodeuteros  | 10000  | Myriad                   |
