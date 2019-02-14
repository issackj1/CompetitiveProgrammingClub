num = int(input())
origin = 0

for i in range(num):
    theN = int(input())
    word = str(theN)
    i = len(word) - 1
    while word[i] == "0":
        i -= 1
    this = int(word[i]) - 1
    elem = i

    newWord = ""
    for i in range(len(word)):
        if i == elem:
            newWord += str(this)
        else:
            newWord += word[i]
    print(int(newWord))
