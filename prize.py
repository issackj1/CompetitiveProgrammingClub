num = list(map(int, input().split()))
items = num[0]
maxCost = num[1]
theNums = list(map(int, input().split()))
theNums.sort()

result = 1;
for i in range(1,items):
    if(theNums[i-1] + theNums[i] <= maxCost):
        result+= 1

print(result)
