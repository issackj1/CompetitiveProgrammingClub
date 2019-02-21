word = input()
result = ""

for i in range(len(word)):
    if word[i].istitle():
        result += word[i]


print(result)
