
rows = int(input())

i = 0
word = []
nums = []
for i in range(rows):
    word.append(input())

for i in range (len(word)):
    nums.append(list(map(int, word[i].split())))

for i in range(rows):
    count = 0
    sum = 0
    cols = nums[i][0]
    for j in range(cols):
        sum += nums[i][j+1]
    average = sum / cols
    num = 0
    for j in range(cols):
        if nums[i][j+1] > average:
            num += 1
    print("%2.3f" % ((num / cols) * 100) + "%")
