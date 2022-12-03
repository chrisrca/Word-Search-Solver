# enchant to compare word to english dictionary
import enchant
d = enchant.Dict("en_US")

# word search chart as list of lists
wordSearch = [ ["E", "L", "D", "U", "U", "P", "M", "G", "W", "W", "V", "C", "L", "Z", "J", "V", "K", "G", "U", "C", "X", "K", "N"],
               ["V", "Q", "N", "J", "V", "M", "R", "N", "N", "H", "S", "R", "T", "C", "J", "D", "N", "A", "L", "S", "I", "V", "K"],
               ["Z", "V", "J", "E", "M", "I", "D", "I", "M", "V", "X", "I", "J", "L", "T", "C", "K", "V", "M", "Z", "J", "Q", "K"],
               ["G", "X", "U", "V", "D", "X", "H", "R", "E", "C", "R", "S", "B", "R", "H", "P", "E", "F", "O", "B", "P", "X", "T"],
               ["N", "Y", "G", "P", "P", "K", "E", "E", "L", "H", "D", "T", "S", "F", "O", "C", "B", "R", "R", "V", "B", "L", "U"],
               ["K", "A", "W", "R", "A", "T", "V", "T", "V", "J", "R", "I", "C", "K", "U", "B", "B", "F", "D", "F", "H", "D", "N"],
               ["N", "A", "F", "O", "I", "B", "W", "A", "I", "V", "H", "A", "Y", "Z", "S", "L", "B", "O", "G", "J", "K", "W", "F"],
               ["R", "M", "Q", "B", "N", "U", "G", "C", "N", "G", "S", "N", "G", "V", "E", "V", "B", "H", "M", "W", "V", "X", "K"],
               ["W", "Y", "B", "K", "T", "W", "Z", "E", "S", "N", "U", "G", "E", "T", "T", "W", "W", "C", "O", "D", "Q", "J", "N"],
               ["A", "Q", "B", "R", "B", "L", "S", "T", "A", "U", "L", "A", "K", "E", "O", "L", "O", "F", "M", "O", "S", "Z", "K"],
               ["F", "V", "I", "I", "A", "G", "D", "L", "R", "H", "F", "L", "M", "L", "U", "V", "M", "U", "J", "Z", "D", "F", "T"],
               ["L", "C", "D", "A", "L", "Y", "J", "O", "U", "K", "T", "L", "H", "T", "R", "Z", "D", "X", "G", "Q", "Y", "M", "A"],
               ["L", "P", "S", "H", "L", "U", "U", "P", "S", "N", "E", "A", "S", "N", "S", "B", "N", "F", "S", "S", "Y", "G", "K"],
               ["L", "L", "F", "C", "G", "X", "K", "I", "H", "A", "G", "R", "T", "U", "I", "Y", "E", "N", "O", "C", "B", "Y", "M"],
               ["N", "I", "R", "S", "E", "Y", "H", "H", "P", "I", "P", "D", "I", "A", "H", "R", "B", "L", "K", "G", "X", "B", "J"],
               ["X", "T", "Z", "M", "H", "I", "J", "C", "X", "V", "J", "O", "L", "G", "E", "P", "Q", "P", "J", "H", "A", "A", "B"] ]

# all possible words
possibleWords = []

# ignore words if they are not at least minsize long
minsize = 4

# recursively increase word size to the left and up to check for words 
def upLeft(x, y, wordSoFar):
    if (x-1 >= 0 and y-1 >= 0):
        if (d.check(wordSoFar + wordSearch[x-1][y-1]) and len(wordSoFar + wordSearch[x-1][y-1]) >= minsize):
            possibleWords.append(wordSoFar + wordSearch[x-1][y-1])
        upLeft(x-1, y-1, wordSoFar + wordSearch[x-1][y-1])

# recursively increase word size to the right and up to check for words 
def upRight(x, y, wordSoFar):
    if (x-1 >= 0 and y+1 < len(wordSearch[0])):
        if (d.check(wordSoFar + wordSearch[x-1][y+1]) and len(wordSoFar + wordSearch[x-1][y+1]) >= minsize):
            possibleWords.append(wordSoFar + wordSearch[x-1][y+1])
        upRight(x-1, y+1, wordSoFar + wordSearch[x-1][y+1])

# recursively increase word size to the left and down to check for words 
def downLeft(x, y, wordSoFar):
    if (x+1 < len(wordSearch) and y-1 >= 0):
        if (d.check(wordSoFar + wordSearch[x+1][y-1]) and len(wordSoFar + wordSearch[x+1][y-1]) >= minsize):
            possibleWords.append(wordSoFar + wordSearch[x+1][y-1])
        downLeft(x+1, y-1, wordSoFar + wordSearch[x+1][y-1])

# recursively increase word size to the left and up to check for words 
def downRight(x, y, wordSoFar):
    if (x+1 < len(wordSearch) and y+1 < len(wordSearch[0])):
        if (d.check(wordSoFar + wordSearch[x+1][y+1]) and len(wordSoFar + wordSearch[x+1][y+1]) >= minsize):
            possibleWords.append(wordSoFar + wordSearch[x+1][y+1])
        downRight(x+1, y+1, wordSoFar + wordSearch[x+1][y+1])

# recursively increase word size left to check for words 
def left(x, y, wordSoFar):
    if (y-1 >= 0):
        if (d.check(wordSoFar + wordSearch[x][y-1]) and len(wordSoFar + wordSearch[x][y-1]) >= minsize):
            possibleWords.append(wordSoFar + wordSearch[x][y-1])
        left(x, y-1, wordSoFar + wordSearch[x][y-1])

# recursively increase word size right to check for words 
def right(x, y, wordSoFar):
    if (y+1 < len(wordSearch[0])):
        if (d.check(wordSoFar + wordSearch[x][y+1]) and len(wordSoFar + wordSearch[x][y+1]) >= minsize):
            possibleWords.append(wordSoFar + wordSearch[x][y+1])
        right(x, y+1, wordSoFar + wordSearch[x][y+1])

# recursively increase word size up to check for words 
def up(x, y, wordSoFar):
    if (x-1 >= 0):
        if (d.check(wordSoFar + wordSearch[x-1][y]) and len(wordSoFar + wordSearch[x-1][y]) >= minsize):
            possibleWords.append(wordSoFar + wordSearch[x-1][y])
        up(x-1, y, wordSoFar + wordSearch[x-1][y])

# recursively increase word size down to check for words 
def down(x, y, wordSoFar):
    if (x+1 < len(wordSearch)):
        if (d.check(wordSoFar + wordSearch[x+1][y]) and len(wordSoFar + wordSearch[x+1][y]) >= minsize):
            possibleWords.append(wordSoFar + wordSearch[x+1][y])
        down(x+1, y, wordSoFar + wordSearch[x+1][y])

# check all directions on every letter in array
for ix, x in enumerate(wordSearch):
    for iy, y in enumerate(x):
        upLeft(ix+1, iy+1, "")
        upRight(ix+1, iy-1, "")
        downLeft(ix-1, iy+1, "")
        downRight(ix-1, iy-1, "")
        left(ix, iy+1, "")
        right(ix, iy-1, "")
        up(ix+1, iy, "")
        down(ix-1, iy, "")

# print found words
for w in possibleWords:
    print(w)