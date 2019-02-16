num = list(map(int, input().split()))
num.sort()

order = input().lower()
result = ""

def appendA():
    global result
    result+=str(num[0])

def appendB():
    global result
    result+= str(num[1])
def appendC():
    global result
    result+= str(num[2])

options = {
    'a':appendA,
    'b':appendB,
    'c':appendC,
}

options[order[0]]()
result += " "
options[order[1]]()
result += " "
options[order[2]]()

print(result)
