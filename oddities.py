rows = int(input())
num = []

i = 0
for i in range(rows):
    num.append(int(input()))

for i in range(rows):
    if num[i] % 2 == 0:
        print("%d is even" % (num[i]))
    else:
        print("%d is odd" % (num[i]))
