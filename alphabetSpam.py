sentence = input()

whitespace = 0
lowercase = 0
uppercase = 0
symbols = 0
num = len(sentence)
for i in range(num):
    if sentence[i] == '_':
        whitespace += 1
    elif sentence[i].islower():
        lowercase += 1
    elif sentence[i].isupper():
        uppercase += 1
    elif ord(sentence[i]) >= 33 and ord(sentence[i]) <= 126:
        symbols += 1
print(whitespace / num)
print(lowercase / num)
print(uppercase / num)
print(symbols / num)
