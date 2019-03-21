word = input()
guess = input()
moves = 10
towin = len(word)

for i in range(len(guess)):
    the = guess[i]
    right = False
    for j in range(len(word)):
        if word[j] == the:
            towin-=1
            right = True
    if right == False:
        moves -= 1
    
    if towin == 0:
        print ('WIN')
        break
    if moves == 0:
        print('LOSE')
        break
