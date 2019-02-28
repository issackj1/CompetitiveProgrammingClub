days = int(input())

for i in range(days):
    if(theNums[i-1] + theNums[i] <= maxCost):
        result+= 1
