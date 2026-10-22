import random

iText = " "
with open('/Users/erichembling/Downloads/Markov/Markov.txt.txt', 'r') as file:
    iText = file.read()
uWords = set()
punctuation = '!?.,'
extras = ')("":;][}{#/$%-`'



for mark in punctuation:
    iText = iText.replace(mark, " " + mark)
    
for mark in extras:
    iText = iText.replace(mark, "")

cText = iText.lower().split()

for word in cText:
    uWords.add(word)

    
numWords = len(uWords)+1

wordMatrix = [[0 for word in range(numWords)] for word in range(numWords)]

count = 1
for word in uWords:
   wordMatrix[count][0] = word
   wordMatrix[0][count] = word
   count += 1
    
   
def searchWord(sInput):
    sCount = 1
    for word in uWords:
        if sInput == word:
            return sCount
        sCount+=1

def printMatrix(matrix):
    col_width = max(len(str(word)) for word in uWords) + 2
    
    for row in matrix:
        print("".join(str(element).ljust(col_width) for element in row))

        
def setProbability():
    for i in range(len(cText)):
        cWord = cText[i]
        if(i < len(cText)-1):
            nWord = cText[i+1]
            wordMatrix[searchWord(cWord)][searchWord(nWord)] += 1

    
setProbability()

def textGenerator(word, sentences, result=None):
    if result is None:
       result = [word]
    if sentences == 0:
        print(" ".join(result))
        return
    
    total = 0
    wIndex = searchWord(word)
    for i in range(numWords):
        if(i < numWords-1):
            total += wordMatrix[wIndex][i+1]
    if total != 0:
        rand = random.randint(1,total)
        for i in range(numWords):
            if(i < numWords-1):
                rand -= wordMatrix[wIndex][i+1]
                if(rand <= 0):
                    nextWord = (wordMatrix[0][i+1])
                    result.append(nextWord)
                    if nextWord in '!?.':
                        textGenerator(nextWord, sentences -1, result)
                    else:
                        textGenerator(nextWord, sentences, result)
                    return


i = 0
while i <= 4:
    randIndex = random.randint(0,numWords)
    while wordMatrix[0][randIndex] in punctuation:
        randIndex = random.randint(0,numWords)

    textGenerator(wordMatrix[0][randIndex], 5)
    print(" ")
    print(" ")
    i += 1