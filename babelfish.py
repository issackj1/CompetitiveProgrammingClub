keys = []
values = []
check = ""
word = []

thend = False
while(thend == False):
    check = input()
    if(check == "" or check==" "):
        thend = True
    else:
        word = check.split()
        values.append(word[0])
        keys.append(word[1])

dictionary = dict(zip(keys, values))

thendd = False
while (thendd == False):
    check = input()
    if(check in dictionary.keys()):
        print(dictionary[check])
    else:
        print("eh")
